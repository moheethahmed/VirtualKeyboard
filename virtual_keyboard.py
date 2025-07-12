import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math
from playsound import playsound
import threading

# Play sound in background
def play_click_sound():
    threading.Thread(target=playsound, args=("click.wav",), daemon=True).start()

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Set larger screen
frame_width = 1280
frame_height = 720
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

# Keyboard layout
keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"],
    ["Space", "Backspace", "Enter"]
]

final_text = ""

def draw_keyboard(img):
    key_positions = []
    start_y = 150
    for i, row in enumerate(keys):
        start_x = 50
        for j, key in enumerate(row):
            if key == "Space":
                w = 300
            elif key == "Backspace":
                w = 160
            elif key == "Enter":
                w = 160
            else:
                w = 80
            h = 60
            x = start_x
            y = start_y + i * 100
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, key, (x + 20, y + 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
            key_positions.append((key, x, y, w, h))
            start_x += w + 10
    return img, key_positions

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, key_positions = draw_keyboard(img)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            if lm_list:
                index_finger = lm_list[8]
                middle_finger = lm_list[12]

                cv2.circle(img, index_finger, 10, (0, 255, 255), cv2.FILLED)

                for key, x, y, w, h in key_positions:
                    if x < index_finger[0] < x + w and y < index_finger[1] < y + h:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), -1)
                        cv2.putText(img, key, (x + 20, y + 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

                        if distance(index_finger, middle_finger) < 40:
                            play_click_sound()

                            if key == "Backspace":
                                final_text = final_text[:-1]
                                pyautogui.press("backspace")
                            elif key == "Space":
                                final_text += " "
                                pyautogui.press("space")
                            elif key == "Enter":
                                final_text += "\n"
                                pyautogui.press("enter")
                            else:
                                final_text += key
                                pyautogui.press(key.lower())

                            cv2.waitKey(300)

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display text
    cv2.rectangle(img, (50, 40), (1200, 100), (50, 50, 50), -1)
    cv2.putText(img, final_text[-80:], (60, 90), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
