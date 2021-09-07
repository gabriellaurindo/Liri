#Imports
import cv2
import glob
import shutil

#Vars
out = len(glob.glob('out\*'))

#Constants
DEC = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

if glob.glob('img\*.jpg'):
   for file in glob.glob('img\*.jpg'):
      img = cv2.imread(file)
      img_cz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      detc = DEC.detectMultiScale(img_cz, scaleFactor=1.3) 
      for(x, y, l, a)in detc:
         cv2.rectangle(img, (x, y), (x + l, y + a), (0,255,0), 1)
      cv2.imwrite('out\img' + str(out) + '.jpg', img)
      out = out + 1 
      shutil.move(file,'.\old')
else :
   print('Sem imagens para reconhecer')
