import cv2
import mediapipe as mp
import sys

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

FINGERTIP_IDS = [4, 8, 12, 16, 20]
FINGER_NAMES = ["Большой", "Указательный", "Средний", "Безымянный", "Мизинец"]

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Ошибка: не удалось открыть камеру.")
        sys.exit(1)

    with mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    ) as hands:
        print("Камера запущена. Нажмите 'q' для выхода.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Ошибка получения кадра.")
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            h, w, _ = frame.shape

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        landmark_drawing_spec=mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                        connection_drawing_spec=mp_draw.DrawingSpec(color=(200, 100, 0), thickness=2)
                    )

                    for i, tip_id in enumerate(FINGERTIP_IDS):
                        lm = hand_landmarks.landmark[tip_id]
                        x, y = int(lm.x * w), int(lm.y * h)

                        cv2.circle(frame, (x, y), 8, (0, 0, 255), -1)
                        cv2.putText(frame, f"{FINGER_NAMES[i]}: ({x},{y})",
                                    (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 255, 255), 1, cv2.LINE_AA)

            cv2.imshow("Отслеживание пальцев", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
