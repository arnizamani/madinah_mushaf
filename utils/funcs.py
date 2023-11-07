from typing import List


def lines(text: str) -> List[str]:
    return text.split('\n')


def unlines(text_lines: List[str]) -> str:
    return '\n'.join(text_lines)
