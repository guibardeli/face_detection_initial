import cv2

def desenhar_rosto(frame, faces, ROI_X1, ROI_Y1, ROI_X2, ROI_Y2):
    # Desenha a ROI
    cv2.rectangle(frame, (ROI_X1, ROI_Y1), (ROI_X2, ROI_Y2), (255, 0, 0), 2)  # ROI em azul

    for (x, y, w, h) in faces:
        # Desenha o retângulo verde ao redor da face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame, "Pessoa Detectada!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Verifica se a face está dentro da ROI
        if (x >= ROI_X1 and x + w <= ROI_X2 and y >= ROI_Y1 and y + h <= ROI_Y2):
            cv2.putText(frame, "Rosto na ROI", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    return frame

