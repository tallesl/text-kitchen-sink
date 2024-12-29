#!/usr/bin/env python3

from sys import stdin, stdout

chunk_size = 8192

while True:
    chunk = stdin.read(chunk_size)

    if not chunk:
        break

    stdout.write(chunk.lower())

