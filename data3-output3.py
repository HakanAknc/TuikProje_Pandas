import pandas as pd

# CSV dosyasını oku
file_path = 'veriSeti_duzensiz_csv/data3.csv'
df = pd.read_csv(file_path, skiprows=4, delimiter=';')  # İlk 4 satırı atla ve ';' ile ayrılmış

# Gereksiz sütunları ve satırları temizle
df = df.dropna(axis=1, how='all')  # Tüm değerleri NaN olan sütunları kaldır
df = df.dropna(how='all')  # Tüm değerleri NaN olan satırları kaldır

# Sütun isimlerini ayarla ve İngilizce terimleri kaldır
df.columns = ['Yıl', 
              '16-24 Toplam', '16-24 Erkek', '16-24 Kadın',
              '25-34 Toplam', '25-34 Erkek', '25-34 Kadın', 
              '35-44 Toplam', '35-44 Erkek', '35-44 Kadın',
              '45-54 Toplam', '45-54 Erkek', '45-54 Kadın', 
              '55-64 Toplam', '55-64 Erkek', '55-64 Kadın',
              '65-74 Toplam', '65-74 Erkek', '65-74 Kadın']

# Son iki satırı sil
df = df[:-2]

# İngilizce terimleri içeren ilk satırı kaldır
df = df.drop(0)

# Temizlenen veriyi göster
print(df.head())

# Temizlenen veriyi yeni bir CSV dosyasına kaydet
cleaned_file_path = 'veriSeti_duzenli_csv/output3.csv'
df.to_csv(cleaned_file_path, index=False)

print("CSV dosyası başarıyla temizlendi ve kaydedildi.")
