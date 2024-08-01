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
                    file_name = csv_files[file_index].replace('.csv', '')
                    
                    # Dosya yolunu oluştur
                    file_path = os.path.join(csv_folder, csv_files[file_index])

                    # Dosyanın var olup olmadığını kontrol et
                    if os.path.isfile(file_path):
                        print(f"{csv_files[file_index]} dosyası bulundu. İlk 5 verisi gösteriliyor...")
                        
                        # Dosyayı oku
                        df = pd.read_csv(file_path)
                        
                        # İlk 5 veriyi göster
                        print(df.head())
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
