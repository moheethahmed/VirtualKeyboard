# VirtualKeyboard
A virtual keyboard using OpenCV, Mediapipe, and PyAutoGUI

# 🖐️ Virtual Keyboard using Hand Gestures (OpenCV + MediaPipe)

This project is a **virtual keyboard** built with **OpenCV**, **MediaPipe**, and **PyAutoGUI**. It uses your **webcam** to detect hand gestures and simulates key presses when your **index** and **middle fingers** come close on a key. A click sound provides feedback for each press.

---

## 📹 Demo
> *(Add your GIF or YouTube link here)*

---

## 🧠 How It Works

### ✅ Hand Detection
- Uses **MediaPipe Hands** to detect and track the hand landmarks.
- Specifically uses the **index finger tip (landmark 8)** and **middle finger tip (landmark 12)** to detect clicks.

### ✅ Keyboard Layout
- A custom virtual keyboard is drawn using OpenCV shapes.
- The layout includes alphabets, **Space**, **Backspace**, and **Enter**.

### ✅ Press Detection
- When the **index finger tip is over a key** and is close to the **middle finger tip**, it counts as a "press".
- A click sound is played and the corresponding key is typed using **pyautogui**.

---

## 🛠️ Requirements

Install all dependencies using:

```bash
pip install opencv-python mediapipe pyautogui numpy playsound
You also need to place a click.wav file in the same directory for audio feedback.


🧾 Code Explanation
🔁 Main Loop
Captures webcam frames and flips them for a mirror effect.

Processes the frame using MediaPipe to detect hand landmarks.

🎯 draw_keyboard(img)
Draws rectangles and text to form a visual keyboard on the screen.

Calculates and returns key positions for later click detection.

📏 distance(p1, p2)
Computes the Euclidean distance between two finger tips.

Used to detect the "click" gesture (fingers close together).

✋ Landmark Logic
Landmark 8 (index tip) is used to point at a key.

Landmark 12 (middle tip) is used for detecting proximity to trigger a click.

🖱️ Key Press Logic
When the index finger is inside a key rectangle and the distance to the middle finger is small:

The key is highlighted (green).

A click sound is played in a separate thread.

The key character is added to final_text and simulated using pyautogui.

🧾 Text Display
Displays the last few characters typed at the top of the screen.

Shows what has been typed using the virtual keyboard.

🔊 Audio Feedback
Uses playsound to play a click.wav file every time a key is pressed.
This improves the realism and responsiveness of the virtual keyboard.

📌 Notes
Only one hand is tracked (you can change max_num_hands to 2 if needed).

The cv2.waitKey(300) adds a delay to avoid repeated key presses.

Make sure your webcam has good lighting and contrast for better accuracy.

📃 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Developed by Shaik Moheeth Ahmed
Feel free to connect or fork this project!
