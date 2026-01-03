# Favicon Oluşturucu

Bir fotoğraftan arka planı kaldırıp kare favicon oluşturmak için iki adımlı basit bir araç.

## Kurulum
```bash
pip install rembg pillow
```

## Kullanım

### 1. Arka Planı Kaldır
```bash
python background_remover.py
```

- `foto.jpg` dosyanızı script ile aynı klasöre koyun
- Script `foto_no_bg.png` dosyası oluşturacak

### 2. Favicon Oluştur
```bash
python create_favicon.py
```

- `foto_no_bg.png` dosyasını kare olarak kırpar
- `favicon.png` olarak kaydeder

## Dosya Yapısı
```
├── foto.jpg              # Giriş (sizin resminiz)
├── background_remover.py # 1. Adım
├── create_favicon.py     # 2. Adım
├── foto_no_bg.png        # Ara çıktı
└── favicon.png           # Final çıktı
```

## Not

- Giriş dosyası herhangi bir formatta olabilir (jpg, png, vb.)
- Çıktı her zaman PNG olmalıdır (şeffaflık için)
- İkinci script görüntüyü ortadan kırparak kare yapar
