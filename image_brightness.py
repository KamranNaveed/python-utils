import os
from PIL import Image, ImageEnhance
folderPath = r''  # Insert file path


for filename in os.listdir(folderPath):
    split_tuple = os.path.splitext(filename)
    if split_tuple[1] == '.jpg':
        file = filename
        img = Image.open()
        filter = ImageEnhance.Brightness(img)
        new_image = img.filter(1.2)
