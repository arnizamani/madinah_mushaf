"""Python code to convert Madinah Mushaf edition of Quran to Unicode-compliant text

The latest code and the converted Quran text can be downloaded from:
https://github.com/arnizamani/madinah_mushaf

"""
from utils.constants import *
from utils.funcs import lines, unlines

SOURCE_PATH = 'madinah_mushaf_hafs_raw.txt'
TARGET_PATH = 'madinah_mushaf_hafs.txt'


def read_source():
    with open(SOURCE_PATH, mode='r', errors='raise', encoding='utf-8') as obj:
        text = obj.read()
        return unlines(
            [line for line in lines(text) if not line.startswith('#')]
        )


def save_result(text: str) -> None:
    with open(TARGET_PATH, mode='w', errors='raise', encoding='utf-8') as obj:
        obj.write(text)


def main():
    source = read_source()
    print(len(source))

    result: str = source
    save_result(result)


if __name__ == "__main__":
    main()
