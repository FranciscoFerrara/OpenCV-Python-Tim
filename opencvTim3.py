import numpy as np
import cv2

cap = cv2.VideoCapture(0) # isso ta selecionando a minha webcam mas caso eu quisesse um video baixado no meu pc, era só colocar o path dele no argumento

while True:
    ret, frame = cap.read() # tem varios argumentos desse cap.get, na documentação é só ver qual o int q representa cada 
    width = int(cap.get(3))  #3 = width
    height = int(cap.get(4)) #4 = height

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #nesses casos não da pra girar por 90 graus pq o width trocaria com o height e acabaria com td kkkk
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # mesma coisa
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image) # mesma coisa do 1

    if cv2.waitKey(1) == ord('q'): # aqui eu só aviso q a tela n deve ser fechada enqt eu não der quit(q)
        break

cap.release()
cv2.destroyAllWindows()  #mesma coisa do 1