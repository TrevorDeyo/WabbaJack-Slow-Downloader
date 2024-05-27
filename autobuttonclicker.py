import pyautogui
import time
import keyboard

counter = 0
def click_button(button):
    pyautogui.click(button.left + button.width // 2, button.top + button.height // 2)
    global counter
    counter += 1
    print(f"Button 1 clicked ({counter} times)")
    time.sleep(1.5)

while True:
    if keyboard.is_pressed('esc'):
        break
    try:
        found_button1 = pyautogui.locateOnScreen('button.png')
        if found_button1:
            click_button(found_button1)

        found_button2 = pyautogui.locateOnScreen('graybutton.png')
        if found_button2:
            click_button(found_button2)

    except pyautogui.ImageNotFoundException:
        print("Image not found. Retrying in 1 second...")
        time.sleep(1)

print("Exiting")
