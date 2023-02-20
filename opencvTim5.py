import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  
    height = int(cap.get(4)) #daqui pra cima eu copiei do ultimo video

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # aqui a gnt converte de bgr pra hsv
    lower_blue = np.array([90, 50, 50]) # só selecionando um tipo mais claro de azul
    upper_blue = np.array([130, 255, 255]) # mesma coisa mas com azul escuro

    mask = cv2.inRange(hsv, lower_blue, upper_blue) # criando uma mascara tipo photoshop mas no python

    result = cv2.bitwise_and(frame, frame, mask=mask) #aqui sendo sincero a explicação n ficou mto clara mas isso mostra o resultado 

    cv2.imshow('frame', result) # mostra a mascara com a cor certa (selecionada) q
    cv2.imshow('mask', mask) # mostra o resultado em branco

    if cv2.waitKey(1) == ord('q'):   # essas ultimas como sempre copiadas dos outros tutoras
        break

cap.release()
cv2.destroyAllWindows()