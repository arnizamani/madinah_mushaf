# pylint: disable=missing-module-docstring,missing-function-docstring,consider-using-enumerate
import re
from configparser import ConfigParser
from typing import List
from .constants import *
from .common import lines, unlines, strip_whitespace
from .tests import test_spacing_did_not_change_contents

BISMILLAH_LINES = (
    'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ ۝١',
    'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ',
    'بِّسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ'
)


def _format_surah_title(line: str, surah_number: int, config: ConfigParser) -> str:
    surah_title = line
    if config.getboolean('Surah', 'show_surah_numbers'):
        surah_title = surah_title + ' ' + str(surah_number)

    if config.getboolean('Surah', 'brackets_around_surah_names'):
        surah_title = BRACKET_START + surah_title + BRACKET_END

    return surah_title


def _format_surah_names(text: str, config: ConfigParser) -> str:
    text_lines = lines(text)
    surah_count = 0
    for i in range(len(text_lines)):
        if text_lines[i].startswith(SURAH_WORD):
            surah_count += 1
            text_lines[i] = _format_surah_title(text_lines[i], surah_count, config)
    assert surah_count == SURAH_COUNT
    return unlines(text_lines)


def _insert_end_of_ayah(text: str) -> str:
    return re.sub('([٠-٩]+)', '۝\\1', text)


def newline_after_end_of_ayah(text: str) -> str:
    text_lines = lines(text)
    newlines = []
    for i in range(len(text_lines)):
        text_lines[i] = re.sub('(۝[٠-٩]+) ', '\\1{NEWLINE}', text_lines[i])
        newlines.extend(text_lines[i].split('{NEWLINE}'))
    return strip_whitespace(unlines(newlines))


def join_multiline_ayah(text: str) -> str:
    text_lines = lines(text)
    newlines = []
    start = ''
    for i in range(len(text_lines)):
        if text_lines[i].startswith(BRACKET_START)\
            or text_lines[i] in BISMILLAH_LINES\
            or (END_OF_AYAH in text_lines[i] and not start):
            newlines.append(text_lines[i])
        elif not start:  # A line without END_OF_AYAH is the first part of a broken ayah line
            start = text_lines[i]
        else:
            if END_OF_AYAH in text_lines[i]:
                newlines.append(start + ' ' + text_lines[i])
                start = ''
            else:
                start = start + SPACE + text_lines[i]
    return unlines(newlines)


def join_ayah_numbers_broken_between_lines(text: str) -> str:
    text_lines = lines(text)
    newlines = []
    for i in range(len(text_lines)):
        text_lines[i] = re.sub('^[٠-٩]* ', '', text_lines[i])
        if i < len(text_lines) - 1 and re.match('^[٠-٩]+ ', text_lines[i+1]):
            number_at_start_of_next_line = text_lines[i+1].split(' ')[0]
            text_lines[i] = text_lines[i] + number_at_start_of_next_line
        newlines.append(text_lines[i])
    return unlines(newlines)


def _format_ayah_lines(text: str, config: ConfigParser) -> str:
    """Format one ayah per line."""
    text = _insert_end_of_ayah(text)
    text = newline_after_end_of_ayah(text)

    text = join_multiline_ayah(text)

    text = join_ayah_numbers_broken_between_lines(text)
    return text


def format_spacing(text: str, config: ConfigParser) -> str:
    text = strip_whitespace(text)
    assert len(lines(text)) == 9046
    text = _format_surah_names(text, config)
    text= _format_ayah_lines(text, config)
    text = text.translate(WESTERN_TO_ARABIC)
    text = text.translate(URDU_TO_ARABIC)
    return text


def make_unicode_compliant(text: str, config: ConfigParser) -> str:
    newtext = format_spacing(text, config)
    test_spacing_did_not_change_contents(text, newtext)

    return newtext
