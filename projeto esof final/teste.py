import cv2
import numpy as np


img = cv2.imread('barra.png',0)#le a imagem em escala de cinza
img2 = cv2.imread('barra.png',1)# le a mesma imagem colorida
tamY, tamX = img.shape
for i in range(tamY):
    for j in range(tamX):
        if img[i,j]<21:
            pix0=0
            pix1=0
            pix2=0
        else:
            pix0=255
            pix1=255
            pix2=255
        img2[i,j][0]=pix0
        img2[i,j][1]=pix1
        img2[i,j][2]=pix2
cv2.imshow('imagem preto e brnco',img2)
cv2.imwrite('pretoEbranco.png',img2)#salva a img preto e branco
