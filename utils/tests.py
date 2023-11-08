# pylint: disable=missing-module-docstring,missing-function-docstring,wildcard-import,unused-wildcard-import
import re
from .common import lines, words, unwords, strip_whitespace
from .constants import *


def _test_line_count(text: str):
    assert len(lines(text)) == SURAH_COUNT + AYAAT_COUNT + BISMILLAH_COUNT


def _test_surah_count(text):
    assert len([line for line in lines(text) if line.startswith(BRACKET_START)]) == SURAH_COUNT


def _test_ayah_count(text):
    assert len(re.findall(END_OF_AYAH, text)) == AYAAT_COUNT
    assert len([line for line in lines(text) if END_OF_AYAH in line]) == AYAAT_COUNT


def _test_bismillah_count(text: str):
    assert len(re.findall(f'{BEH}({SHADDA})?{KASRA}سۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', text)) == SURAH_COUNT


def _strip_non_text_chars(text: str) -> str:
    text = re.sub(END_OF_AYAH, '', text)
    text = re.sub(BRACKET_START, '', text)
    text = re.sub(BRACKET_END, '', text)
    text = re.sub('[٠١٢٣٤٥٦٧٨٩]', '', text)
    text = strip_whitespace(text)
    return text


def test_spacing_did_not_change_contents(old_text: str, new_text: str):
    old_text = _strip_non_text_chars(old_text)
    new_text = _strip_non_text_chars(new_text)
    assert unwords(lines(old_text)) == unwords(lines(new_text))


def run_final_tests(old_text: str, new_text: str) -> None:
    _test_line_count(new_text)
    _test_surah_count(new_text)
    _test_ayah_count(new_text)
    _test_bismillah_count(new_text)
