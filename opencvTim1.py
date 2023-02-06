import cv2
#Carregar a imagem
img_igro = cv2.imread('assets/igrovac.jpg', 0) 
#Parametros:
#1° Image Path   
#2° Tags  ==  Colorido = -1 / Preto e Branco = 0 / Sem mudar = 1

img_igro = cv2.resize(img_igro,(0,0), fx=2, fy=2)#parametros: 1° img   2° tamanho    ou    usar fx e fy (multiplica a quantidade atual de pixel por x) 
img_igro_ = cv2.rotate(img_igro, cv2.ROTATE_180) #se quiser mais opção ve na documentação  / até rimou


cv2.imshow('Imagem', img_igro)#Parametros: 1° WinLabel  2° Image
cv2.waitKey(0)#Essa linha espera que qualquer tecla seja apertada por uma quantidade de tempo colocada no parametro para continuar rodando o código
cv2.destroyAllWindows()#Essa linha é auto explicativa kakkakka