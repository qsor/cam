import cv2
import time

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
        if not cap.isOpened():
            print("Ошибка: камера не найдена")
            return

    print("g - ч/б режим, s - сохранить кадр, q - выход")

    fps_start = time.time()
    frame_count = 0
    fps = 0.0
    gray_mode = False



if __name__ == "__main__":
    main()
