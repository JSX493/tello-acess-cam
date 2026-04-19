from djitellopy import Tello
import cv2
import time

def iniciar_camera_tello():
    # Inicializa o objeto do drone
    tello = Tello()

    try:
        # Conecta ao drone (via Wi-Fi do Tello)
        tello.connect()
        
        # Garante que o stream de vídeo esteja ligado
        tello.streamon()
        
        print(f"Bateria: {tello.get_battery()}%")
        print("Pressione 'q' para sair.")

        while True:
            # Captura o frame atual do stream
            frame = tello.get_frame_read().frame
            
            # Redimensiona (opcional) para melhor visualização
            img = cv2.resize(frame, (640, 480))
            
            # Exibe a imagem na janela
            cv2.imshow("Tello Camera Feed", img)

            # Para o loop se a tecla 'q' for pressionada
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"Erro ao conectar: {e}")

    finally:
        # Finaliza os recursos
        tello.streamoff()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    iniciar_camera_tello()