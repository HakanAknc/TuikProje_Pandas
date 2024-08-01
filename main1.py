import pandas as pd
import os

# CSV dosyalarının bulunduğu klasör
csv_folder = 'veriSeti_duzenli_csv/'

def list_csv_files(folder):
    # Verilen klasördeki tüm CSV dosyalarını listele
    return [f for f in os.listdir(folder) if f.endswith('.csv')]

while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1 - CSV dosyalarını listele ve çek")
    print("2 - Çıkış")

    # Kullanıcıdan işlem seçeneği alın
    choice = input("Seçiminizi yapın: ")

    if choice == '1':
        # Mevcut CSV dosyalarını listele
        csv_files = list_csv_files(csv_folder)
        
        if csv_files:
            print("\nMevcut CSV dosyaları:")
            for i, file in enumerate(csv_files, start=1):
                print(f"{i} - {file}")
            
            try:
                # Kullanıcıdan dosya numarasını seçmesini iste
                file_index = int(input("\nİşlem yapmak istediğiniz CSV dosyasının numarasını girin: ")) - 1
                
                if 0 <= file_index < len(csv_files):
                    # Dosya yolunu oluştur
                    file_path = os.path.join(csv_folder, csv_files[file_index])

                    # Dosyanın var olup olmadığını kontrol et
                    if os.path.isfile(file_path):
                        print(f"{csv_files[file_index]} dosyası bulundu. Yıl ve kolon bilgisi alınıyor...")

                        # Dosyayı oku
                        df = pd.read_csv(file_path)
                        
                        # Kolon adlarını normalize et (boşlukları alt çizgi ile değiştir)
                        df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

                        # Kullanıcıya mevcut yılları ve kolonları göster
                        unique_values = df.iloc[:, 0].unique()
                        columns = [col for col in df.columns if col != df.columns[0].lower()]

                        print("Mevcut Satırlar:")
                        print(unique_values)
                        print("\nMevcut Sütunlar:")
                        print(columns)

                        # Kullanıcıdan yıl ve kolon adı al
                        try:
                            value = input(f"\n{df.columns[0]} girin: ")
                            if df[df.columns[0]].dtype == 'int64':
                                value = int(value)
                        except ValueError:
                            print("Lütfen geçerli bir değer girin.")
                            continue

                        column = input("Kolon adı girin: ").strip().replace(' ', '_').lower()

                        def get_value(value, column):
                            # İlk kolon adının kullanılmasını engelle
                            if column == df.columns[0].lower():
                                return "Geçersiz kolon adı"

                            try:
                                # Verilen değer için filtrele
                                row = df[df[df.columns[0].lower()] == value]

                                # Belirli bir kolonun değerini al
                                if column in row.columns:
                                    result = row[column].values[0]
                                    return result
                                else:
                                    return "Geçersiz kolon adı"
                            except IndexError:
                                return "Belirtilen değer bulunamadı"

                        # Fonksiyonu çağır ve sonucu al
                        result = get_value(value, column)

                        # Sonucu yazdır
                        print(f"{value} {df.columns[0]} için {column} verisi: {result}")
                    else:
                        print("Hatalı dosya adı. Lütfen geçerli bir CSV dosyası adı girin.")
                else:
                    print("Geçersiz numara. Lütfen listedeki numaralardan birini seçin.")
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        
        else:
            print("Bu klasörde hiçbir CSV dosyası bulunmuyor.")
    
    elif choice == '2':
        print("Programdan çıkılıyor...")
        break
    
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 girin.")
