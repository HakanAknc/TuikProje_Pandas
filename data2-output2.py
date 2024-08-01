import pandas as pd

# CSV dosyasını oku
file_path = 'veriSeti_duzensiz_csv/data2.csv'
df = pd.read_csv(file_path, skiprows=6)  # İlk 6 satırı atla

# Gereksiz sütunları ve satırları temizle
df = df.dropna(axis=1, how='all')  # Tüm değerleri NaN olan sütunları kaldır

# İlk sütunun adını 'Yıl' olarak değiştir
df.columns = ['Yıl', 'Toplam', 'Otomobil', 'Minibüs', 'Otobüs', 'Kamyonet', 'Kamyon', 'Motosiklet', 'Özel amaçlı taşıtlar', 'Yol ve iş makineleri', 'Traktör']

# İlk satırdaki 'Yıl' verilerini temizleyip, eksik veya hatalı verileri temizleyin
df = df.dropna(subset=['Yıl'])

# Gereksiz metinleri (örneğin, 'Source:', 'Note:', gibi) temizle
df = df[df['Yıl'].str.isnumeric()]

# Yıl sütununu integer tipe çevir
df['Yıl'] = df['Yıl'].astype(int)
df['Toplam'] = df['Toplam'].astype(int)

# '-' ve '- (3)' gibi değerleri 0 ile değiştir
df.replace({'-': 0, '- (3)': 0}, inplace=True)

# NaN değerlerini 0 ile değiştir
df = df.fillna(0)

# Düzenlenen veriyi göster
print(df.head())

# Düzenlenen veriyi yeni bir CSV dosyasına kaydet
cleaned_file_path = 'veriSeti_duzenli_csv/output2.csv'
df.to_csv(cleaned_file_path, index=False)

print("CSV dosyası başarıyla temizlendi ve kaydedildi.")
