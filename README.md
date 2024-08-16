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

## concatenating all .txt

```
$ cat *.txt > all.txt
```

## pre-processing .txt

```
$ chmod +x no-extra-spaces.py en-only.py # or pt-only.py
$ cat all.txt | ./en-only.py | ./no-extra-spaces.py > preprocessed.txt
``` 
