#!/usr/bin/env python3

from collections import Counter
from re import findall
from sys import stdin

text = stdin.read()

total_characters = len(text)
print(f'characters: {total_characters}')

total_lines = text.count('\n') + 1
print(f'lines: {total_lines}')


words = findall(r'\b\w+\b', text.lower())
total_words = len(words)
print(f'words: {total_words}')

word_counter = Counter(words)
unique_words = len(word_counter)
print(f'unique words: {unique_words}')

print()

most_common_words = word_counter.most_common(10)
print('most frequent words:')
for word, count in most_common_words:
    print(f'• {word}: {count}')
