import pyautogui
import time
import keyboard

counter = 0

while True:
    if keyboard.is_pressed('esc'):
        break
    try:
        found_button1 = pyautogui.locateOnScreen('button.png')
        if found_button1:
            pyautogui.click(button.left + button.width // 2, button.top + button.height // 2)
            counter += 1
            print(f"Button clicked ({counter} times)")
            time.sleep(1.5)

    except pyautogui.ImageNotFoundException:
        pyautogui.moveRel(-100, 0)
        print("Image not found. Retrying in 1 second...")
        time.sleep(1)

print("Exiting")
