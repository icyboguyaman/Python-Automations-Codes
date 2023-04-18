import pyautogui
import time

# Wait for the user to position the mouse
input("Position the mouse over the target location and press Enter to continue...")

# Get the current mouse position
x, y = pyautogui.position()

# Move the mouse to the target location
pyautogui.moveTo(x + 100, y + 100, duration=1.0)

# Click the mouse
pyautogui.click()

# Wait for 5 seconds
time.sleep(5)

# Type some text
pyautogui.typewrite("Hello, World!")

# Press Enter
pyautogui.press("enter")
