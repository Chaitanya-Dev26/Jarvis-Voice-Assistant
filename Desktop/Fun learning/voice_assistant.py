import time
import pyautogui
import speech_recognition as sr
import pyttsx3

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
        recognizer.adjust_for_ambient_noise(source, duration=0.5) 
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Can you repeat?")
        return None
    except sr.RequestError:
        speak("There was an error with the voice recognition service.")
        return None

def open_app(app_name, website=None):
    """Opens an app through Spotlight Search and types it automatically."""
    responses = {
        "google": "Opening Google Chrome for you.",
        "youtube": "Sure, opening YouTube for you!",
        "instagram": "Launching Instagram now.",
        "spotify": "Opening Spotify now.",
        "whatsapp": "Launching WhatsApp.",
    }

    speak(responses.get(app_name, f"Opening {app_name}..."))

    # Open Spotlight Search (Cmd + Space)
    pyautogui.hotkey("command", "space")
    time.sleep(0.3)   


    # Type app name
    pyautogui.typewrite(app_name, interval=0.02)
    time.sleep(0.2)

    # Press Enter to open the app
    pyautogui.press("enter")
    time.sleep(1.5)  # Allow the app to load

    # If a website is provided, open it in Chrome
    if website:
        time.sleep(0.5)
        pyautogui.hotkey("command", "l")  # Focus URL bar
        time.sleep(0.2)
        pyautogui.typewrite(website, interval=0.02)
        pyautogui.press("enter")

def main():

    while True:
        command = listen_command()

        if command:
            if "google" in command:
                open_app("Google Chrome")
            elif "youtube" in command:
                open_app("Google Chrome", "https://www.youtube.com")
            elif "instagram" in command:
                open_app("Google Chrome", "https://www.instagram.com")
            elif "spotify" in command:
                open_app("Spotify")
            elif "whatsapp" in command:
                open_app("WhatsApp")
            elif "stop" in command or "exit" in command:
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("I didn't recognize that command. Please say again.")

        speak("What next would you like me to open?")
        time.sleep(0.5)

if __name__ == "__main__":
    main()