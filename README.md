# 🚀 Jarvis Voice Assistant  

A **fun voice assistant project** that lets you **open apps and websites** on **macOS** using **voice commands**! 🎙️ Built for fun, but hey, it actually works! 😎  

---

## 🔹 Features  
✅ **Voice-Controlled App Launcher** – Open apps like Chrome, Spotify, WhatsApp, and more.  
✅ **Web Navigation** – Instantly opens YouTube, Instagram, and other websites.  
✅ **Fully Hands-Free** – Uses **macOS Spotlight (`Cmd + Space`)** for seamless launching.  
✅ **Fast Execution** – Optimized for speed with minimal delays.  
✅ **Stop Command** – Say `"Stop"` or `"Exit"` to quit.  

---

## 🔹 How to Install & Run  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Chaitanya-Dev26/Jarvis-Voice-Assistant.git
   cd Jarvis-Voice-Assistant

2. **Install Dependencies**
   ```bash
   pip install pyautogui SpeechRecognition pyttsx3

2. **Run the Voice Assistant**
   ```bash
   python3 voice_assistant.py

## 🔹 How It Works  

1. The assistant listens to your **voice command**.  
2. It identifies whether you want to **open an app** or **a website**.  
3. If it’s an **app**, it triggers **Spotlight Search** (`Cmd + Space`) and types the app name.  
4. If it’s a **website**, it opens **Chrome** and navigates to the requested URL.  
5. The assistant **keeps asking for the next command** until you say **"Stop"** or **"Exit"**.

## 🔹 Example Commands  

🎙️ Say:  

- `"Open Google"` → Launches **Google Chrome**  
- `"Open YouTube"` → Opens **YouTube in Chrome**  
- `"Open Instagram"` → Opens **Instagram in Chrome**  
- `"Stop"` or `"Exit"` → **Closes the assistant**  

## 🔹 License  
This project is for fun & learning purposes. Use it at your own risk.  

