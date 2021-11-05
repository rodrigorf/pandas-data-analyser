import numpy as np
import pandas as pd

import util as util
from configSetup import config

USE_XLSX = config.getboolean('main','useExcelFile')
SHEET_NAME = config.get('main','excelSheetName')
INVALID_MARKER = config.get('main','invalidValueMarker')

if(USE_XLSX):
    df = pd.ExcelFile('data/input/data.xlsx').parse(SHEET_NAME)
else:
    df = pd.read_csv('data/input/data.csv', sep = ';')

df = df.loc[:, df.columns != 'ORDEM']
df = df.replace(INVALID_MARKER, np.nan)\
    .replace('', np.nan)\
    .replace(r'^\s*$', np.nan, regex=True)
df.round(2)

print('\n===== DATA SAMPLE (first five rows) =====')
print(df.head())

print('\n===== COUNT BY COLUMN (VALID CELLS) =====')
print(df.describe().round(2))

print('\n===== MISSING DATA =====')
percent_missing = df.isna().sum() * 100 / len(df)
missing_value_df = pd.DataFrame({'Percentage (%)': percent_missing})
print(missing_value_df.round(2))

print('\n===== STATS BY COLUMN =====')
for column in df:
    print(f'\nQTD  RANK  GRADE: {column}')
    seriesDataCount = df[column].value_counts(dropna=False)
    for index, value in seriesDataCount.items():
        print(f'{index}    {value}    {util.applyRank(index, value)}')

#TO EXCEL STATS
df.describe().round(2).to_excel("data/output/stats.xlsx")

