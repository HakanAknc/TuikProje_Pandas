import pandas as pd

df = pd.read_csv('veriSeti_duzenli_csv/output4.csv')


# Yazdırma
# print(df)

# ilk beş satır
# print(df.head())

# son beş satır
# print(df.tail())


# Veri çerçevesinin özet bilgilerini göster
# print(df.info())

# Temel istatistiksel bilgileri göster
# print(df.describe())


# -------------------

# Sütun adlarını ve ilk birkaç satırı görüntüle
print("Sütun Adları:")
print(df.columns)

print("\nİlk 5 Satır:")
print(df.head())
