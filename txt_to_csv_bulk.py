import os
import io
import numpy
import pandas as pd

merged_df = pd.DataFrame()
for file in os.listdir("PATH_OF_DIRECTORY"):
    if file.endswith(".txt"):
        bytes = open(file, 'rb').read()
        merged_df = merged_df.append(pd.read_csv(io.StringIO(
            bytes.decode('utf-8')), sep='\t', parse_dates=['Time']))

print(len(merged_df))