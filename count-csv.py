#!/usr/bin/env python3

from sys import argv
from pandas import read_csv  # pip install pandas

print(len(read_csv(argv[1], low_memory=False)))
