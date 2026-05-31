import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
import os
import pyautogui
import g4f  # Free AI library that works like ChatGPT

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Setup voice properties
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Index 1 is usually a female voice
engine.setProperty('rate', 180)  # Speed of speaking

def speak(text):
    """Makes the assistant talk."""
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

def force_close_browser():
    """Forcefully terminates common web browsers directly from the OS."""
    speak("Closing the window.")
    if os.name == 'nt':  # FOR WINDOWS
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im msedge.exe")
        os.system("taskkill /f /im firefox.exe")
    else:  # FOR MAC
        os.system("pkill -f 'Google Chrome'")
        os.system("pkill -f 'Safari'")
        os.system("pkill -f 'Firefox'")

def ask_ai(user_prompt):
    """Sends your voice message to the AI and gets a response."""
    try:
        print("AI is thinking...")
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[
                {"role": "system", "content": "You are a friendly, witty, and concise voice assistant. Keep your answers short (1-2 sentences) so they sound natural when spoken aloud."},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response
    except Exception:
        return "I am having trouble connecting to my brain right now."

def take_command(recognizer, microphone):
    """Listens to your voice and converts it to text."""
    with microphone as source:
        print("\n🎙️ I'm listening to you...")
        recognizer.energy_threshold = 1200  # Normal room sensitivity
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)
            print("Processing voice...")
            command = recognizer.recognize_google(audio, language='en-in').lower()
            print(f"You said: {command}")
            return command
        except Exception:
            return ""

def main():
    r = sr.Recognizer()
    m = sr.Microphone()
    
    speak("Hello! I am ready. We can chat, play music, or close windows.")
    
    while True:
        command = take_command(r, m)

        if not command:
            continue

        # 1. SPECIAL COMMAND: EXIT SCRIPT COMPLETELY
        if "exit" in command or "goodbye" in command:
            speak("Goodbye! Talk to you later.")
            break

        # 2. SPECIAL COMMAND: FORCE CLOSE THE BROWSER WINDOW
        elif "close" in command or "close window" in command:
            force_close_browser()
            time.sleep(2)

        # 3. SPECIAL COMMAND: PLAY MUSIC
        elif "play" in command and not ("pause" in command or "resume" in command):
            song = command.replace("play", "").strip()
            if song:
                speak(f"Sure, playing {song} on YouTube.")
                pywhatkit.playonyt(song)
                time.sleep(5)

        # 4. SPECIAL COMMANDS: YOUTUBE IN-WINDOW CONTROLS
        elif "pause" in command or "resume" in command or "stop" in command:
            pyautogui.press('space')
            print("[System: Toggled Pause]")
            
        elif "mute" in command or "unmute" in command:
            pyautogui.press('m')
            print("[System: Toggled Mute]")

        # 5. CHAT MODE: Talk back naturally
        else:
            ai_reply = ask_ai(command)
            speak(ai_reply)

if __name__ == "__main__":
    main()