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

## Character frequency
Following is a table showing counts of characters in the main text of the Quran (converted file), excluding Surah title lines, whitespace and ayah numbering.

| Char | Unicode | Name | Count |
| ---- | ------- | ---- | ----- |
| َ | U+064e |  | 123502 |
|   | U+0020 |  | 77766 |
| ِ | U+0650 |  | 46741 |
| ل | U+0644 |  | 38550 |
| ُ | U+064f |  | 37454 |
| ۡ | U+06e1 |  | 37372 |
| ن | U+0646 |  | 27380 |
| م | U+0645 |  | 27071 |
| ا | U+0627 |  | 25184 |
| و | U+0648 |  | 24971 |
| ّ | U+0651 |  | 23016 |
| ی | U+06cc |  | 22037 |
| ه | U+0647 |  | 14962 |
| ٱ | U+0671 |  | 13819 |
| ر | U+0631 |  | 12627 |
| ب | U+0628 |  | 11603 |
| ت | U+062a |  | 10520 |
| ك | U+0643 |  | 10497 |
| ٰ | U+0670 |  | 9837 |
| ع | U+0639 |  | 9405 |
| أ | U+0623 |  | 8900 |
| ف | U+0641 |  | 8747 |
| ق | U+0642 |  | 7034 |
| ـ | U+0640 |  | 6850 |
| ۝ | U+06dd |  | 6236 |
| س | U+0633 |  | 6122 |
| د | U+062f |  | 5991 |
| ٓ | U+0653 |  | 5376 |
| إ | U+0625 |  | 5088 |
| ذ | U+0630 |  | 4932 |
| ح | U+062d |  | 4364 |
| ۟ | U+06df |  | 3988 |
| ى | U+0649 |  | 3589 |
| ج | U+062c |  | 3317 |
| ࣰ | U+08f0 |  | 2901 |
| ء | U+0621 |  | 2782 |
| خ | U+062e |  | 2497 |
| ة | U+0629 |  | 2344 |
| ش | U+0634 |  | 2124 |
| ۚ | U+06da |  | 2083 |
| ص | U+0635 |  | 2074 |
| ࣲ | U+08f2 |  | 1935 |
| ࣱ | U+08f1 |  | 1807 |
| ض | U+0636 |  | 1686 |
| ۖ | U+06d6 |  | 1651 |
| ز | U+0632 |  | 1599 |
| ث | U+062b |  | 1414 |
|   | U+202f |  | 1376 |
| ط | U+0637 |  | 1273 |
| ۥ | U+06e5 |  | 1256 |
| غ | U+063a |  | 1221 |
| ۦ | U+06e6 |  | 957 |
| ظ | U+0638 |  | 853 |
| ٔ | U+0654 |  | 773 |
| ً | U+064b |  | 734 |
| ؤ | U+0624 |  | 705 |
| ٕ | U+0655 |  | 690 |
| ٍ | U+064d |  | 599 |
| ٌ | U+064c |  | 578 |
| ۗ | U+06d7 |  | 511 |
| ۢ | U+06e2 |  | 510 |
| ئ | U+0626 |  | 232 |
| ۞ | U+06de |  | 199 |
| ۭ | U+06ed |  | 99 |
| ۠ | U+06e0 |  | 66 |
| ۧ | U+06e7 |  | 38 |
| ۘ | U+06d8 |  | 21 |
| ۩ | U+06e9 |  | 15 |
| ۜ | U+06dc |  | 8 |
| ۛ | U+06db |  | 6 |
| ۬ | U+06ec |  | 2 |
| ࢭ | U+08ad |  | 1 
| ٜ | U+065c |  | 1 |
| ࣳ | U+08f3 |  | 1 |
| ۨ | U+06e8 |  | 1 |
