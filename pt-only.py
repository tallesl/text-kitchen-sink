#!/usr/bin/env python3

from sys import stdin, stdout

chunk_size = 8192
allowed = set('\n !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÇÈÉÊÌÍÎÒÓÔÕÙÚÛÜàáâãçèéêìíîòóôõùúûü—“”…')

while True:
    chunk = stdin.read(chunk_size)

    if not chunk:
        break

    stdout.write(''.join(char for char in chunk if char in allowed))
