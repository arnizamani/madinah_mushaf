# pylint: disable=missing-module-docstring,missing-function-docstring
import re
from .constants import SPACE
from typing import List


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
