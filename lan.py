import numpy as np
from PIL import Image

# Görseli yükle
img_path = 'foto_no_bg.png'
img = Image.open(img_path)

# Boyutları al
width, height = img.size

# Kare yapmak için kırpılacak alanı hesapla (Ortala)
new_size = min(width, height)
left = (width - new_size) / 2
top = (height - new_size) / 2
right = (width + new_size) / 2
bottom = (height + new_size) / 2

# Kırp
img_cropped = img.crop((left, top, right, bottom))

# Favicon genelde png tercih edilir, png olarak kaydet
output_path = 'favicon.png'
img_cropped.save(output_path)
