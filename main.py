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

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Ошибка захвата")
                break

            frame_count += 1
            now = time.time()
            if now - fps_start >= 1.0:
                fps = frame_count / (now - fps_start)
                frame_count = 0
                fps_start = now

            display = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if gray_mode else frame

            text = f"FPS: {fps:.1f} | {'B/W' if gray_mode else 'COLOR'}"
            color = (255, 255, 255) if gray_mode else (0, 255, 0)
            cv2.putText(display, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            cv2.imshow("Camera", display)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('g'):
                gray_mode = not gray_mode
            elif key == ord('s'):
                cv2.imwrite(f"shot_{int(time.time())}.jpg", frame)
                print("Сохранено")

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
