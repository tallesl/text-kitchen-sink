#!/usr/bin/env python3

# pip install pandas

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
df_deduped = df.drop_duplicates(subset=df.columns[3], keep='first')
print(df_deduped.to_csv(index=False))
