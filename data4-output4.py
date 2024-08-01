import pandas as pd

# CSV dosyasını oku (ilk 10 satırı atlayarak başlıkları temizleyin)
file_path = 'veriSeti_duzensiz_csv/data4.csv'
df = pd.read_csv(file_path, skiprows=2)

# Son iki satırı sil
df = df[:-8]

# Gereksiz sütunları temizle
#df = df.drop(columns=['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], errors='ignore')

# Sütun isimlerini düzenle
df.columns = ['Yıl', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']

# 'Toplam' satırını ve diğer gereksiz satırları temizle
df = df[df['İl'].notna()]

# 'İl' sütununda ve diğer sütunlarda NaN veya '-' olan değerleri 0 ile değiştir
df = df.replace({'-': 0, 'NaN': 0})

# Sütunları uygun türdeki verilere dönüştür
df['2023'] = pd.to_numeric(df['2023'], errors='coerce').fillna(0).astype(int)
df['2024'] = pd.to_numeric(df['2024'], errors='coerce').fillna(0).astype(int)
df['2025'] = pd.to_numeric(df['2025'], errors='coerce').fillna(0).astype(int)
df['2026'] = pd.to_numeric(df['2026'], errors='coerce').fillna(0).astype(int)
df['2027'] = pd.to_numeric(df['2027'], errors='coerce').fillna(0).astype(int)
df['2028'] = pd.to_numeric(df['2028'], errors='coerce').fillna(0).astype(int)
df['2029'] = pd.to_numeric(df['2029'], errors='coerce').fillna(0).astype(int)
df['2030'] = pd.to_numeric(df['2030'], errors='coerce').fillna(0).astype(int)

# Düzenlenen veriyi göster
print(df.head())

# Düzenlenen veriyi yeni bir CSV dosyasına kaydet
cleaned_file_path = 'veriSeti_duzenli_csv/output5.csv'
df.to_csv(cleaned_file_path, index=False)

print("CSV dosyası başarıyla temizlendi ve kaydedildi.")
