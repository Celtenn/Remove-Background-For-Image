# pip install rembg pillow
from rembg import remove
from PIL import Image

def background_remover(input_path, output_path):
    try:
        # Resmi aç
        input_image = Image.open(input_path)
        
        # Arka planı kaldır
        print("İşlem yapılıyor, lütfen bekleyin...")
        output_image = remove(input_image)
        
        # Çıktıyı kaydet
        output_image.save(output_path)
        print(f"Başarılı! Arka planı silinmiş resim şuraya kaydedildi: {output_path}")
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# KULLANIM:
# 'foto.jpg' yerine kendi resim dosyanızın adını yazın.
# Çıktı mutlaka .png olmalı (şeffaflık desteği için).
if __name__ == "__main__":
    giris_resmi = "foto.jpg"      # Kaynak dosya
    cikis_resmi = "foto_no_bg.png" # Çıktı dosyası (PNG olmalı)
    
    background_remover(giris_resmi, cikis_resmi)