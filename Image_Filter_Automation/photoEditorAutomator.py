#Abhay
#Project tool used to automate images with a specific filter, constrast and other settings.
from PIL import Image, ImageEnhance, ImageFilter
import os

path ='./imgs'
pathOut = '/editedImgs'
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    factor = 1.5
    enhancer = enhancer.enhance(factor)
    clean_name = os.path.splittext(filename)[0]
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
