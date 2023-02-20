import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  
    height = int(cap.get(4)) # daqui pra cima eu copiei do ultimo video
    
    # só lembrando que assim como no pyautogui, o plano cartesiano do opencv tem o 0, 0 marcados no canto esquerdo superior da tela/imagem

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) # desenha uma linha na imagem  |  o 1° parametro é a imagem que queremos editarde coordenada até coordenada que vai fazer a linha
    # o 3° é a cor da linha, lembra que não eh RGB e sim BGR e o ultimo argumento é a 
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5) # mesma coisa do de cima soq pro outro lado
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5) #os 3 primeiros argumentos são iguais os outros, já o 4 quando se trata de figuras que podem ser preenchidas, ao invés de somente definir a thickness, pode tambem preencher a figura colocando -1
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)# argumentos: imagm | posição central | raio do circ | thickness/preenchimento
    font = cv2.FONT_HERSHEY_SIMPLEX # é só pegar a fonte, não achei nenhuma legal ;-;
    img = cv2.putText(img, 'Igro Careca Vac', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)# argumentos: imagem | texto | canto esquerdo inferior da image | fonte | cor | Thickness e cv2LINE_AA, segundo o tim e a propria documentação isso deixa a letra mais bonita akakakakaka

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):  # essas ultimas linhas são iguais as outras
        break

cap.release()
cv2.destroyAllWindows()