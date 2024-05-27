import pyautogui
import time
import keyboard

def locate_custom_object():
    custom_object = None
    while custom_object is None:
        # Replace 'button.png' with the path to your custom image
        custom_object = pyautogui.locateOnScreen('button.png')
    return custom_object

counter = 0
while not esc_pressed:
    if keyboard.is_pressed('esc'):
        break
    try:
        found_object = locate_custom_object()
        if found_object:
            # Perform an action (e.g., click on the found object)
            pyautogui.click(found_object.left + found_object.width // 2, found_object.top + found_object.height // 2)
            print("clicked successes", counter)
            counter += 1
            time.sleep(1.5)
    except pyautogui.ImageNotFoundException:
        # Handle the case when the image is not found
        print("Image not found. Retrying in 1 second...")
        time.sleep(1.5)  # Wait for 1 second before checking again