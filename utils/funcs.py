# pylint: disable=missing-module-docstring,missing-function-docstring,consider-using-enumerate
import re
from copy import copy
from configparser import ConfigParser
from typing import List
from .constants import *
from .common import lines, unlines, strip_whitespace, is_surah_heading, replace_and_assert
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
        if is_surah_heading(text_lines[i])\
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


def _format_ayah_lines(text: str) -> str:
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
    text= _format_ayah_lines(text)
    text = text.translate(WESTERN_TO_ARABIC)
    if config.getboolean('Ayah', 'use_urdu_digits'):
        text = text.translate(ARABIC_TO_URDU)
    return text


def unicode_compliance(text: str) -> str:
    """Convert non-Unicode characters to their Unicode counterparts"""
    text = replace_and_assert(text, '\u0657', '\u08F0', chars=2901) # Open fathatan
    text = replace_and_assert(text, '\u065E', '\u08F1', chars=1807) # Open dammatan
    text = replace_and_assert(text, '\u0656', '\u08F2', chars=1935) # Open kasratan
    text = replace_and_assert(text, '\u06E4', '', length=-26)
    text = replace_and_assert(text, '\u0652', '\u06DF', chars=3988) # Sukun -> Small High Rounded Zero
    return text


def fix_superscript_alef(text: str) -> str:
    """
    Add tatweel or spacing character before superscript alef so it appears to the left of the
    base letter.
    """
    count = 7412
    assert text.count(f'{FATHA}{SUP_ALEF}') == count, text.count(f'{FATHA}{SUP_ALEF}')
    newtext = copy(text)
    for key, value in FATHA_HIGHALEF_REPLACEMENTS:
        newtext = re.sub(key, value, newtext)
        newtext = re.sub(key, value, newtext)

    assert len(text) == len(newtext) - count
    return newtext


def spelling_corrections(text: str, config: ConfigParser) -> str:
    # Insert Small High Waw with Maddah Above in only one word Li-Yasoo'oo
    text = replace_and_assert(text, 'سُـُٔو', 'سُـࣳٓــُٔو', words=1)

    # Convert Yeh to Urdu Yeh (dotless form)
    text = replace_and_assert(text, '\u064A', '\u06CC', chars=22057)

    # Fix Lam-Alef
    text = replace_and_assert(text, '\u0623\u0653', '\u0640\u0654\u064E\u0627', words=277)

    # Fix Faddaraatum
    text = replace_and_assert(
        text, f'{SUP_ALEF}{HAMZA_ABOVE}', f'\u08AD{HAMZA_ABOVE}{SUKUN}', words=1, length=1)

    # Fix Ta'amanna
    text = replace_and_assert(
        text, f'{FATHA}{FILLED_DOT_ABOVE}', f'{FATHA}{TATWEEL}{FILLED_DOT_ABOVE}',
        words=1, length=1)

    # Move Hamza-Kasra to below baseline
    text = replace_and_assert(
        text, YEH_HAMZA_ABOVE + KASRA, ALEF_MAQSURA + HAMZA_BELOW + KASRA, words=676)

    if config.getboolean('Format', 'horizontal_placement_of_alef_saghira'):
        text = fix_superscript_alef(text)
    return text


def make_unicode_compliant(text: str, config: ConfigParser) -> str:
    newtext = format_spacing(text, config)
    test_spacing_did_not_change_contents(text, newtext)

    text = unicode_compliance(newtext)

    text = spelling_corrections(text, config)

    return text
