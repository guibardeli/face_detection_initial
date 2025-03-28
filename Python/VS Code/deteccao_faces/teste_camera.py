import cv2

print("Iniciando camera...")

cap = cv2.VideoCapture(0)  # Teste com 1

if not cap.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
else: 
    print("Webcam acessada com sucesso!")

cap.release()
cv2.destroyAllWindows()
