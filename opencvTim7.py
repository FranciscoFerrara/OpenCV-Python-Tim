import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8) # tem que dar resize nas duas images pq se não não detecta direito por motivos obveos
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape  # pega altura e largura da imagem da shuteira

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]  #aqui tem 6 metodos diferentes pra achar a shuteira, alguns são mais eficazes, outros menos todos tão explicados na documentação

for method in methods: # vai loopar pra checar e ver cada um dos metodos
    img2 = img.copy() # esse comando vai criar uma copia onde eu vou poder desenhar o quadrado sem afetar a imagem real oficial

    result = cv2.matchTemplate(img2, template, method)# isso vai usar o matchTemplate pra "caminhar" pela imagem buscando por uma combinação mais certeira de acordo com os metodos
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:                            #ta loopando
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)       # mostra as paradas
    cv2.waitKey(0)
    cv2.destroyAllWindows()