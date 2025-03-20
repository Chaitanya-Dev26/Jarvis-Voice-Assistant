import time
import pyautogui

def open_youtube_via_spotlight():
    # Open Spotlight Search (Cmd + Space)
    pyautogui.hotkey("command", "space")
    time.sleep(1)  # Reduced delay

    # Type 'Google Chrome' in Spotlight
    pyautogui.typewrite("Google Chrome", interval=0.05)  # Faster typing
    time.sleep(0.7)  # Shorter wait

    # Press Enter to open Chrome
    pyautogui.press("enter")
    time.sleep(2.5)  # Optimized wait time for Chrome to launch

    # Bring Chrome to focus & open address bar (Cmd + L)
    pyautogui.hotkey("command", "l")
    time.sleep(0.3)  # Quick pause

    # Type 'youtube.com' and press Enter
    pyautogui.typewrite("youtube.com", interval=0.05)
    pyautogui.press("enter")

    print("YouTube is opening in Google Chrome...")

# Run the faster automation
open_youtube_via_spotlight()