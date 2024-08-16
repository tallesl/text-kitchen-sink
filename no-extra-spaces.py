#!/usr/bin/env python3

from sys import stdin, stdout

chunk_size = 8192
last_char = None

while True:
    chunk = stdin.read(chunk_size)
    if not chunk:
        break

    output_chunk = []
    for char in chunk:
        if char not in (' ', '\n') or last_char != char:
            output_chunk.append(char)
        last_char = char

    stdout.write(''.join(output_chunk))

# ensure the final character is output correctly
if last_char in (' ', '\n'):
    stdout.write(last_char)
