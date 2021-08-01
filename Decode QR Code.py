from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(r'D:\Video_block\Python_program\Python Mini Project\QRcode.png')
result = decode(img)

print(result)