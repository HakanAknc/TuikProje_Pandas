import pandas as pd

file_path = "veriSeti_duzensiz_csv/data1.csv"
df = pd.read_csv(file_path)

df = df.fillna(1)

print(df.head())