"""
import pandas as pd

xls_file_path = 'dosya adı.xls'

data = pd.read_excel(xls_file_path)

csv_file_path = 'dosya adı.csv'
data.to_csv(csv_file_path, index=False)

print(f"{xls_file_path} dosyası başarıyla {csv_file_path} olarak kaydedildi.")
"""


# Kodumu bir Fonskiyon içine aldım yukardakinden daha derli toplu oldu
import pandas as pd

def convert_xls_to_csv(xls_file_path, csv_file_path):
    data = pd.read_excel(xls_file_path)
    data.to_csv(csv_file_path, index=False)
    print(f"{xls_file_path} dosyası başarıyla {csv_file_path} olarak kaydedildi.")

xls_file_path = 'veriSeti_xls/2Motorlu kara taşıt sayısı.xls'
csv_file_path = 'veriSeti_csv/data2.csv'
convert_xls_to_csv(xls_file_path, csv_file_path)
