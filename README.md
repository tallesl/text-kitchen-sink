# Text kitchen sink

Pre-processing text for future cool stuff.

## .pdf to .txt

```
$ sudo apt install poppler-utils
$ for f in *.pdf; do echo "Processing $f"; pdftotext "$f"; done
```

## .mobi to .txt

```
$ sudo apt install calibre
$ for f in *.mobi; do echo "Processing $f"; ebook-convert "$f" "${f%.mobi}.txt"; done
```

## .prc to .txt

```
$ sudo apt install calibre
$ for f in *.prc; do echo "Processing $f"; ebook-convert "$f" "${f%.prc}.txt"; done
```

## .txt concatenation

```
$ cat *.txt > all.txt
```

## .txt pre-processing

```
$ chmod +x no-extra-spaces.py en-only.py # or pt-only.py
$ cat all.txt | ./en-only.py | ./no-extra-spaces.py > preprocessed.txt
``` 

## .txt statistics

``` 
characters: 741
lines: 4
words: 140
unique words: 84

most frequent words:
• is: 8
• the: 8
• and: 6
• it: 6
• its: 5
• charmander: 4
• a: 4
• pokemon: 4
• when: 4
• in: 3
``` 

## directory search and flattening

```
$ chmod +x find-and-flatten.py
$ ./find-and-flatten.py 'crawled_forum/' 'flattened_directory/' 'thread-*.html'
```

## file sampling

```
$ chmod +x find-and-flatten.py
$ ./sample-files.py 'crawled_forum/' 'crawled_samples/' 15
```

## scraping to .csv

```
$ chmod +x scrap_to_csv.py
$ pip install beautifulsoup4 tdqm
$ ./scrap-to-csv.py 'crawled_forum/' '.forum .post .post-content'
$ head -n 1 scrap.csv
uuid,directory,file,content
```

## deduping .csv by "content" column

```
$ chmod +x dedupe.py
$ pip install pandas
$ ./dedupe.py scrap.csv > deduped.csv
```
