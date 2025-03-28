import cv2

# Carregando o modelo Haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detectar_faces(frame):
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza, menos 'informações' para análise
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.3, minNeighbors=8, minSize=(20, 20)) 

    return faces  # Retorna o frame processado e as faces detectadas