#!/usr/bin/env python3

from re import sub
from sys import argv, exit, stdin

def extract_ngrams(text, n):
    text = sub(r'[^a-zãáâêéíîóôõúç]', ' ', text) # replace non-alpha
    
    words = text.split() # split into spaces
    
    words = [word for word in words if len(word) >= n] # remove words shorter than N
    
    ngrams = set()
    
    for word in words:
        for i in range(len(word) - n + 1): # ranges for windows of size N
            ngram = word[i:i + n] # extract current window from the word
            ngrams.add(ngram)

    return sorted(ngrams)

if __name__ == "__main__":
    n = int(argv[1])
    input_text = stdin.read().strip().lower()
    ngrams = extract_ngrams(input_text, n)
    
    for ngram in ngrams:
        print(ngram)
