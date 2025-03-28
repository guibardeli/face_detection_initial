import cv2
import numpy as np
from video_capture import iniciar_captura
from face_detection import detectar_faces
from display import desenhar_rosto



print("O script foi iniciado com sucesso... Aguarde")

def main():
    cam = iniciar_captura()

    if cam is None:
        exit()

    # Configuração do VideoWriter para gravar o vídeo processado
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  #Salvar o vídeo 
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Define o arquivo de saída

    # Define a ROI (Região de Interesse)
    ROI_X1, ROI_Y1, ROI_X2, ROI_Y2 = 150, 100, 450, 400  # Ajuste conforme necessário

    while True:
        ret, frame = cam.read()

        if not ret or frame is None: #add
            print("Erro ao capturar frame da webcam")
            break


        faces = detectar_faces(frame)

        # Aplica borramento nos rostos detectados, mas somente se estiverem dentro da ROI
        for (x, y, w, h) in faces:
            # Verifica se a face está completamente dentro da ROI
            if x >= ROI_X1 and y >= ROI_Y1 and x + w <= ROI_X2 and y + h <= ROI_Y2:
                # Aplica o borramento se a face estiver dentro da ROI
                face_region = frame[y:y + h, x:x + w]  # Região da face
                frame[y:y + h, x:x + w] = cv2.GaussianBlur(face_region, (99, 99), 30)  # Aplica o borramento


        # Desenha a caixa da face e aplica a ROI e alerta
        frame = desenhar_rosto(frame, faces, ROI_X1, ROI_Y1, ROI_X2, ROI_Y2)
        

        cv2.imshow("Detecting faces", frame)


    # Grava o frame processado no arquivo de saída
        out.write(frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' para sair
            break

    cam.release()
    out.release()
    cv2.destroyAllWindows()

    
if __name__ == "__main__":
     main()