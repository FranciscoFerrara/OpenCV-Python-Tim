import cv2
import random

img = cv2.imread('assets/igrovac.jpg', -1)
img = cv2.resize(img,(0,0), fx=2, fy=2)
# Opencv não usa RGB(red,green,blue) ele usa BGR(blue,green,red)
# imagens são interpretadas por pixeis, esses pixeis e suas cores são definidos por diversas e diversas arrays
# quando usamos o cv2.rotate não estamos simplesmente girando uma imagem, estamos na verdade rotacionando e rearranjando os dados de cada umas dessas arrays

#for i in range(50):                               # mudar os pixeis de uma parte da img pra cores aleatorias
#    for j in range(img.shape[1]):                  
#        img[i][j] = [random.randrange(255),random.randrange(255),random.randrange(255)]

tag = img[10:60, 80:130] # transforma variavel tag em uma parte especifica da img
img[110:160, 30:80] = tag # faz com que esse parte da img se torne oq era em tag
# basicamente ctrl c ctrl v soq em img kkkkk

cv2.imshow('Imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()