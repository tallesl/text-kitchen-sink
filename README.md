# Text Kitchen Sink

Pre-processing text for future cool stuff.

## .xxx to .txt

`.pdf` to `.txt`:

```
$ sudo apt install poppler-utils
$ for f in *.pdf; do echo "Processing $f"; pdftotext "$f"; done
```

`.mobi` to `.txt`:

```
$ sudo apt install calibre
$ for f in *.mobi; do echo "Processing $f"; ebook-convert "$f" "${f%.mobi}.txt"; done
```

`.prc` to `.txt`:

```
$ sudo apt install calibre
$ for f in *.prc; do echo "Processing $f"; ebook-convert "$f" "${f%.prc}.txt"; done
```

## .txt

From utf-8 to latin-1:

```
$ cat utf8.txt | iconv -c -f UTF-8 -t ISO-8859-1//IGNORE > latin1.txt
```

Concatenation:

```
$ cat *.txt > all.txt
```

Pre-processing:

```
$ chmod +x no-extra-spaces.py en-only.py # or pt-only.py
$ cat all.txt | ./en-only.py | ./no-extra-spaces.py | ./lower.py > preprocessed.txt
``` 

Statistics:

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

## crawled .html to scraped .csv

Directory search and flattening:

```
$ chmod +x find-and-flatten.py
$ ./find-and-flatten.py 'crawled_forum/' 'flattened_directory/' 'thread-*.html'
```

File sampling:

```
$ chmod +x sample-files.py
$ ./sample-files.py 'crawled_forum/' 'crawled_samples/' 15
```

Scraping to `.csv`:

```
$ chmod +x scrap_to_csv.py
$ pip install beautifulsoup4 tdqm
$ ./scrap-to-csv.py 'crawled_forum/' '.postbody .content div'
$ head -n 1 scrap.csv
uuid,directory,file,content
```

Scraping recipe:

1. Inspect the filepaths looking for a common pattern (`find crawled.com/ | vim -`).
1. [Find the files and flat the directory](#directory-search-and-flattening).
1. [Take some samples](#file-sampling).
1. Inspect the HTML samples looking for what to extract, figuring it out what CSS selector will do the job.
1. [Scrap the samples to .csv](#scraping-to-csv).
1. Inspect the .csv, check if it looks correct.
1. If yes, now scrap again but this time on all the crawled pages. If not, back to figuring it out the CSS selector.

## .csv cleanup

Counting rows:

```
$ sudo apt install csvkit
$ csvstat --count scrap.csv
```

Viewing "content" column only:

```
$ sudo apt install csvkit
$ cat scrap.csv | csvcut -c 4 --maxfieldsize 999999 | less
```

Use sed to remove any line containing things such as "CRITEO TAG", "upload picture", ".jpg", etc:

```
$ sed -i '/FISHY STRING GOES HERE$/d' scrap.csv
```

Using sed to remove extension:

```
$ sed -E -i '
/\.html/ {      # match ".html"
    s/\.html//  # remove ".html"
}' scrap.csv
```

Use sed to remove query string:

```
$ sed -E -i '
/viewtopic\.php\?/ { # match "viewtopic.php?"
    s/\?.*?,/,/      # remove from "?" up to the next ","
}' scrap.csv
```

Checking if the file is well-formed:

```
$ sudo apt install csvkit
$ csvclean -n scrap.csv
```

Deduping rows by "content" column:

```
$ ./dedupe-by-content.py scrap.csv > deduped.csv
```
