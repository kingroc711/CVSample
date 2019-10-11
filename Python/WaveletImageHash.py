import PIL
from PIL import Image
import imagehash

lenna400 = PIL.Image.open('./res/lenna400x400.jpg')
lenna512 = PIL.Image.open('./res/lenna512x512.png')
lennaText = PIL.Image.open('./res/lenna317x360_add_text.jpg')

p = imagehash.phash(lenna400)
p1 = imagehash.phash(lenna512)
p2 = imagehash.phash(lennaText)
print('phash leanna400  : ', p)
print('phash leanna512  : ', p1)
print('phash leannatext : ', p2)
print('phash leanna400 compare leanna512  : ', (p - p1) / len(p.hash) ** 2)
print('phash leanna400 compare leannatext : ', (p - p2) / len(p.hash) ** 2)
print('phash leanna512 compare leannatext : ', (p1 - p2) / len(p1.hash) ** 2, end='\n\n')

w = imagehash.whash(lenna400)
w1 = imagehash.whash(lenna512)
w2 = imagehash.whash(lennaText)
print('whash leanna400  : ', w)
print('whash leanna512  : ', w1)
print('whash leannatext : ', w2)
print('whash leanna400 compare leanna512  : ', (w - w1)/len(w.hash)**2)
print('whash leanna400 compare leannatext : ', (w - w2)/len(w.hash)**2)
print('whash leanna512 compare leannatext : ', (w1 - w2)/len(w1.hash)**2, end='\n\n')

a = imagehash.average_hash(lenna400)
a1 = imagehash.average_hash(lenna512)
a2 = imagehash.average_hash(lennaText)
print('average_hash leanna400  : ', a)
print('average_hash leanna512  : ', a1)
print('average_hash leannatext : ', a2)
print('average_hash leanna400 compare leanna512  : ', (a - a1)/len(a.hash)**2)
print('average_hash leanna400 compare leannatext : ', (a - a2)/len(a.hash)**2)
print('average_hash leanna512 compare leannatext : ', (a1 - a2)/len(a1.hash)**2, end='\n\n')

d = imagehash.dhash(lenna400)
d1 = imagehash.dhash(lenna512)
d2 = imagehash.dhash(lennaText)
print('dhash leanna400  : ', d)
print('dhash leanna512  : ', d1)
print('dhash leannatext : ', d2)
print('dhash leanna400 compare leanna512  : ', (d - d1) / len(d.hash) ** 2)
print('dhash leanna400 compare leannatext : ', (d - d2) / len(d.hash) ** 2)
print('dhash leanna512 compare leannatext : ', (d1 - d2) / len(d1.hash) ** 2)

