import cv2
import glob
import shutil

imgs = [cv2.imread(file) for file in glob.glob('img\*.jpg')]
out = [cv2.imread(file) for file in glob.glob('out\*.jpg')]
c = len(out)
for img in imgs:
   dec = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
   img_cz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   detc = dec.detectMultiScale(img_cz, scaleFactor=1.3) 
   for(x, y, l, a)in detc:
      cv2.rectangle(img, (x, y), (x + l, y + a), (0,255,0), 1)
   cv2.imwrite('out\img' + str(c) + '.jpg', img)
   c = c + 1   
for file in glob.glob('img\*.jpg'):
   shutil.move(file,'.\old')
