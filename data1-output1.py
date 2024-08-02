import pandas as pd

# CSV dosyasını oku
file_path = 'veriSeti_duzenli_csv/.csv'  # Dosya yolunuzu buraya ekleyin
df = pd.read_csv(file_path, delimiter=';')  # ";" ile ayrılmış verileri oku

# Veriyi "," ile ayrılmış olarak kaydet
# output_file_path = 'data_converted.csv'  # Çıktı dosya yolunuzu buraya ekleyin
# df.to_csv(output_file_path, sep=',', index=False)

# print("Veri başarıyla dönüştürüldü ve kaydedildi.")


# 'Unnamed: 0' ve 'Unnamed: 1' sütunlarını kaldır
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 1'])

# Veriyi , ile ayırarak kaydet
output_file_path = 'veriSeti_duzenli_csv/data1.csv'  # Çıktı dosya yolunuzu buraya ekleyin
df.to_csv(output_file_path, sep=',', index=False)

print("Veri başarıyla dönüştürüldü, NaN değerleri silindi ve kaydedildi.")