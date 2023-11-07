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

## Fonts 
Not all Arabic-script fonts have support for the complete characterset of the Quran. Following fonts can be used to properly visualize the converted text:

* Scheherazade New (by SIL)
* Lateef (by SIL)
* Paktype Naskh (by Lateef Sagar Shaikh)
