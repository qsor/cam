import cv2
import time

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
        if not cap.isOpened():
            print("Ошибка: камера не найдена")
            return



if __name__ == "__main__":
    main()
