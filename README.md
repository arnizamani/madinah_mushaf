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
| َ | U+064E | FATHA | 123502 |
| ِ | U+0650 | KASRA | 46741 |
| ل | U+0644 | LAM | 38550 |
| ُ | U+064F | DAMMA | 37454 |
| ۡ | U+06E1 | SMALL HIGH DOTLESS HEAD OF KHAH | 37372 |
| ن | U+0646 | NOON | 27380 |
| م | U+0645 | MEEM | 27071 |
| ا | U+0627 | ALEF | 25184 |
| و | U+0648 | WAW | 24971 |
| ّ | U+0651 | SHADDA | 23016 |
| ی | U+06CC | FARSI YEH | 22037 |
| ه | U+0647 | HEH | 14962 |
| ٱ | U+0671 | ALEF WASLA | 13819 |
| ر | U+0631 | REH | 12627 |
| ب | U+0628 | BEH | 11603 |
| ت | U+062A | TEH | 10520 |
| ك | U+0643 | KAF | 10497 |
| ٰ | U+0670 | SUPERSCRIPT ALEF | 9837 |
| ع | U+0639 | AIN | 9405 |
| أ | U+0623 | ALEF WITH HAMZA ABOVE | 8900 |
| ف | U+0641 | FEH | 8747 |
| ق | U+0642 | QAF | 7034 |
| ـ | U+0640 | TATWEEL | 6850 |
| ۝ | U+06DD | END OF AYAH | 6236 |
| س | U+0633 | SEEN | 6122 |
| د | U+062F | DAL | 5991 |
| ٓ | U+0653 | MADDAH ABOVE | 5376 |
| إ | U+0625 | ALEF WITH HAMZA BELOW | 5088 |
| ذ | U+0630 | THAL | 4932 |
| ح | U+062D | HAH | 4364 |
| ۟ | U+06DF | SMALL HIGH ROUNDED ZERO | 3988 |
| ى | U+0649 | ALEF MAKSURA | 3589 |
| ج | U+062C | JEEM | 3317 |
| ࣰ | U+08F0 | OPEN FATHATAN | 2901 |
| ء | U+0621 | HAMZA | 2782 |
| خ | U+062E | KHAH | 2497 |
| ة | U+0629 | TEH MARBUTA | 2344 |
| ش | U+0634 | SHEEN | 2124 |
| ۚ | U+06DA | SMALL HIGH JEEM | 2083 |
| ص | U+0635 | SAD | 2074 |
| ࣲ | U+08F2 | OPEN KASRATAN | 1935 |
| ࣱ | U+08F1 | OPEN DAMMATAN | 1807 |
| ض | U+0636 | DAD | 1686 |
| ۖ | U+06D6 | SMALL HIGH LIGATURE SALAY | 1651 |
| ز | U+0632 | ZAIN | 1599 |
| ث | U+062B | THEH | 1414 |
|   | U+202F | NARROW NO-BREAK SPACE | 1376 |
| ط | U+0637 | TAH | 1273 |
| ۥ | U+06E5 | SMALL WAW | 1256 |
| غ | U+063A | GHAIN | 1221 |
| ۦ | U+06E6 | SMALL YEH | 957 |
| ظ | U+0638 | ZAH | 853 |
| ٔ | U+0654 | HAMZA ABOVE | 773 |
| ً | U+064B | FATHATAN | 734 |
| ؤ | U+0624 | WAW WITH HAMZA ABOVE | 705 |
| ٕ | U+0655 | HAMZA BELOW | 690 |
| ٍ | U+064D | KASRATAN | 599 |
| ٌ | U+064C | DAMMATAN | 578 |
| ۗ | U+06D7 | SMALL HIGH LIGATURE QALAY | 511 |
| ۢ | U+06E2 | SMALL HIGH MEEM ISOLATED FORM | 510 |
| ئ | U+0626 | YEH WITH HAMZA ABOVE | 232 |
| ۞ | U+06DE | START OF RUB EL HIZB | 199 |
| ۭ | U+06ED | SMALL LOW MEEM | 99 |
| ۠ | U+06E0 | SMALL HIGH UPRIGHT RECTANGULAR ZERO | 66 |
| ۧ | U+06E7 | SMALL HIGH YEH | 38 |
| ۘ | U+06D8 | SMALL HIGH MEEM INITIAL FORM | 21 |
| ۩ | U+06E9 | PLACE OF SAJDAH | 15 |
| ۜ | U+06DC | SMALL HIGH SEEN | 8 |
| ۛ | U+06DB | SMALL HIGH THREE DOTS | 6 |
| ۬ | U+06EC | ROUNDED HIGH STOP WITH FILLED CENTRE | 2 |
| ࢭ | U+08AD | LOW ALEF | 1 |
| ٜ | U+065C | VOWEL SIGN DOT BELOW | 1 |
| ࣳ | U+08F3 | SMALL HIGH WAW | 1 |
| ۨ | U+06E8 | SMALL HIGH NOON | 1 |
