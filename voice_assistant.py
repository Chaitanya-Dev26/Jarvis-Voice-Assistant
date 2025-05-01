import time
import pyautogui
import speech_recognition as sr
import pyttsx3
import subprocess
import sys
import platform

engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listens for a voice command and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What would you like me to open?")
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1.0)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Can you repeat?")
        return None
    except sr.RequestError:
        speak("There was an error with the voice recognition service.")
        return None

def trigger_spotlight():
    """Triggers Spotlight Search using AppleScript (only on macOS)."""
    if platform.system() == "Darwin":
        script = 'tell application "System Events" to key code 49 using {command down}'
        subprocess.run(["osascript", "-e", script])
        time.sleep(0.3)
    else:
        speak("Spotlight is only available on macOS.")

def open_app(app_name, website=None):
    """Opens an app through Spotlight Search and types it automatically."""
    responses = {
        "google": "Opening Google Chrome for you.",
        "youtube": "Sure, opening YouTube for you!",
        "instagram": "Launching Instagram now.",
        "spotify": "Opening Spotify now.",
        "whatsapp": "Launching WhatsApp.",
    }

    message = responses.get(app_name.lower(), f"Opening {app_name}...")
    speak(message)
    print(f"{app_name} opened.")  # Display the message in the terminal

    # Trigger Spotlight Search
    trigger_spotlight()

    # Type app name
    pyautogui.typewrite(app_name, interval=0.02)
    time.sleep(0.2)

    # Press Enter to open the app
    pyautogui.press("enter")
    time.sleep(1.5)

    # If a website is provided, open it
    if website:
        time.sleep(0.5)
        pyautogui.hotkey("command", "l")  # Focus URL bar
        time.sleep(0.2)
        pyautogui.typewrite(website, interval=0.02)
        pyautogui.press("enter")

def main():
    command_map = {
        "google": ("Google Chrome", None),
        "youtube": ("Google Chrome", "https://www.youtube.com"),
        "instagram": ("Google Chrome", "https://www.instagram.com"),
        "spotify": ("Spotify", None),
        "whatsapp": ("WhatsApp", None),
    }

    while True:
        command = listen_command()

        if command:
            found = False
            for key in command_map:
                if key in command:
                    app, url = command_map[key]
                    open_app(app, url)
                    found = True
                    break

            if "stop" in command or "exit" in command:
                speak("Goodbye! Have a great day!")
                break

            if not found:
                speak("I didn't recognize that command. Please say again.")

        speak("What next would you like me to open?")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
