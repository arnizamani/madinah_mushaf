# pylint: disable=missing-module-docstring,missing-function-docstring
import re
from typing import List, Optional
from .constants import SPACE, SURAH_WORD, BRACKET_START


def lines(text: str) -> List[str]:
    return text.split('\n')


def unlines(text_lines: List[str]) -> str:
    return '\n'.join(text_lines)


def words(text: str) -> List[str]:
    return text.split()


def unwords(words_list: List[str]) -> str:
    return ' '.join(words_list)


def strip_whitespace(text: str) -> str:
    new_lines = [
        re.sub(f'{SPACE}+', SPACE, line.strip())
        for line in lines(text)
        if line.strip()
    ]
    return unlines(new_lines)


def is_surah_heading(line: str) -> bool:
    return line.startswith(BRACKET_START) or line.startswith(SURAH_WORD)


def count_changed_words(old_text: str, new_text: str) -> int:
    old_words = words(old_text)
    new_words = words(new_text)
    assert len(old_words) == len(new_words)
    return sum(x != y for (x, y) in zip(old_words, new_words))


def count_changed_characters(old_text: str, new_text: str) -> int:
    assert len(old_text) == len(new_text)
    return sum(x != y for (x, y) in zip(old_text, new_text))


# pylint: disable=too-many-arguments
def replace_and_assert(
        text: str,
        from_regex: str,
        to_regex: str,
        chars_changed: Optional[int] = None,
        words_changed: Optional[int] = None,
        length_increase: Optional[int] = None,
        words_increase: Optional[int] = None,
) -> str:
    new_text = re.sub(from_regex, to_regex, text)
    if chars_changed is not None:
        assert count_changed_characters(text, new_text) == chars_changed,\
             count_changed_characters(text, new_text)
    if words_changed is not None:
        assert count_changed_words(text, new_text) == words_changed,\
            count_changed_words(text, new_text)
    if length_increase is not None:
        assert len(text) == len(new_text) - length_increase, len(text) - len(new_text)
    if words_increase is not None:
        assert len(words(text)) == len(words(new_text)) - words_increase,\
            len(words(text)) - len(words(new_text))
    return new_text
