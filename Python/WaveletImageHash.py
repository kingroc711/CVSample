import PIL
from PIL import Image
import imagehash

lenna = PIL.Image.open('./res/lenna400x400.jpg')
lenna1 = PIL.Image.open('./res/lenna512x512.png')

h = imagehash.phash(lenna)
print(h)

h1 = imagehash.phash(lenna1)
print(h1)

print(h-h1)
