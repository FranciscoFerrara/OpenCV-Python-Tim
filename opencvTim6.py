import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.6, fy=0.6)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # os algoritmos detectam coisa desse tipo melhor em gray scale, por isso tem essa modificação


corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # esse nome n eh nem um poko intuitivo kkkk mas resumindo isso usa a detecção de cantos do Shi-Tomasi, um monte de calculo q um dia eu vou aprender
corners = np.int0(corners)   # esses arguments de cima são, Imagem | Qntd de cantos que eu quero | Quanto que o algoritmo tem de ctz que é um canto | distancia absoluta minima entre 2 pontos


for corner in corners:
	x, y = corner.ravel() # aqui vai loopar pra fazer bolinhas nos cantos certeiros
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):  # for it loop basico
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])  # resumindo, todo esse loopzasso vai ligar todos os pontos entre si, preguiça de anotar como funfa
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) # seleciona as cor que vai pintar as linhas
		cv2.line(img, corner1, corner2, color, 1) # faz a linha 

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()