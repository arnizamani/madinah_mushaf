"""Python code to convert Madinah Mushaf edition of Quran to Unicode-compliant text

The latest code and the converted Quran text can be downloaded from:
https://github.com/arnizamani/madinah_mushaf

"""
# pylint: disable=missing-function-docstring
import configparser
from utils.constants import *
from utils.funcs import lines, unlines, make_unicode_compliant
from utils.tests import run_final_tests

CONFIG_PATH = 'config.ini'
SOURCE_PATH = 'madinah_mushaf_hafs_raw.txt'
TARGET_PATH = 'madinah_mushaf_hafs.txt'


def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config


def read_source():
    with open(SOURCE_PATH, mode='r', errors='raise', encoding='utf-8') as obj:
        text = obj.read()
        source = unlines(
            [line for line in lines(text) if not line.startswith('#')]
        )
        source_line_count = len(lines(source))
        print('Source lines', source_line_count)
        assert source_line_count == 9649, "Raw text must contain 9649 lines"
        return source


def save_result(text: str) -> None:
    with open(TARGET_PATH, mode='w', errors='raise', encoding='utf-8') as obj:
        obj.write(text)
    print('Target lines', len(lines(text)))


def main():
    config = read_config()

    source = read_source()

    result: str = make_unicode_compliant(source, config)
    run_final_tests(source, result, config)

    save_result(result)


if __name__ == "__main__":
    main()
