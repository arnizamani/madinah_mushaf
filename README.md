# madinah_mushaf
### Python code to convert Madinah Mushaf edition of Quran to Unicode-compliant text

The Madinah Mushaf edition of the Holy Quran in the Hafs narration is arguably the most read and recited edition of this holy book. It is printed with hand-crafted beautifull calligraphy by "King Fahd Complex for the Printing of the Holy Quran" ([KFCPQ](https://dm.qurancomplex.gov.sa/en/)) of Saudi Arabia.

The same text is also released as text in the docx format, with a custom font attached to it. The font is claimed to be a Unicode font, however it overrides several Unicode characters and is not fully Unicode compliant. The text cannot be properly viewed in any other Unicode-compliant font.

The Python code in this repo converts the raw text released by KFCPQ into text that is fully Unicode-compliant and hence can be copied and viewed properly in other fonts.

## Raw Text
The raw text of the Madinah Mushaf (`madinah_mushaf_hafs_raw.txt`) was retrieved from the word document released by KFCPQ, downloaded 7 November 2023. No changes were made to this text except inserting a few comment lines at the beginning.

## Conversion
The raw text undergoes processing to make it Unicode-compliant by converting some characters to their Unicode variants. Some other modifications are done to make it similar to the printed edition.

Configuration is stored in `config.ini`. Raw text is read from `madinah_mushaf_hafs_raw.txt`.

To run the code:
`python3 main.py`

Results are saved in `madinah_mushaf_hafs.txt`.

## Result
The converted Unicode-compliant text is included here in the file `madinah_mushaf_hafs.txt`.

## Issues
Currently, some software do not show certain character combinations correctly. For example, MS Word does not properly join `Waqf` signs with `U+06DF` (silent character).

When `Hamza` sits between `Lam` and `Alef`, the `Lam-Alef` ligature is not formed correctly in any software. This is a deficiency in Unicode specification. Work is ongoing to fix this.

Most of the modern Arabic fonts place `Shadda+Kasra` above a letter. In Quranic typography, `Kasra` should actually be placed below the letter. Some fonts have an option to override the default behavior in the rendering sofware (e.g. Scheherazade New).
