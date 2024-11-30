#!/usr/bin/env python3

from sys import argv
from pandas import read_csv  # pip install pandas

dataframe = read_csv(argv[1], low_memory=False)
deduped_dataframe = dataframe.drop_duplicates(subset=dataframe.columns[3], keep='first')
print(deduped_dataframe.to_csv(index=False))
