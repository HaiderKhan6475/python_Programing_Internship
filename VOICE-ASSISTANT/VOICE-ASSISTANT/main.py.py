import time
import tempfile
import os
import datetime
import webbrowser
import wikipedia
import re
import subprocess
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

# ---------------------------
# Configuration
# ---------------------------
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
VSCODE_PATH = r"C:\Users\f24ar\AppData\Local\Programs\Microsoft VS Code\Code.exe"
DEFAULT_RECORD_SECONDS = 4

_launched = {}


# ---------------------------
# Text-to-Speech
# ---------------------------
def speak(text):
    print(f"Assistant: {text}")
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)


# ---------------------------
# Utilities
# ---------------------------
def clean_text(text):
    return text.lower().strip()


def extract_query(command, keyword):
    return command.replace(keyword, "").strip()


def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "No information found."


# ---------------------------
# App Control
# ---------------------------
def open_app(app):
    app = app.lower()

    if app == "chrome":
        if os.path.exists(CHROME_PATH):
            _launched[app] = subprocess.Popen([CHROME_PATH])
            return "Opening Chrome"
        webbrowser.open("https://google.com")
        return "Opening browser"

    if app in ["vscode", "vs code", "code"]:
        if os.path.exists(VSCODE_PATH):
            _launched["vscode"] = subprocess.Popen([VSCODE_PATH])
            return "Opening VS Code"
        return "VS Code not found"

    if app == "youtube":
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    return "App not recognized"


def close_app(app):
    app = app.lower()

    if app in _launched:
        process = _launched[app]
        if process.poll() is None:
            process.terminate()
            return f"Closed {app}"

    return "App not running or not opened by me"


# ---------------------------
# Command Processor (SMART)
# ---------------------------
def process_command(command):
    cmd = clean_text(command)

    # Greeting
    if any(x in cmd for x in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"

    if "how are you" in cmd:
        return "I am fine, thank you!"

    # Time & Date
    if "time" in cmd:
        return f"It is {datetime.datetime.now().strftime('%I:%M %p')}"

    if "date" in cmd:
        return f"Today is {datetime.datetime.now().strftime('%B %d, %Y')}"

    # Open Apps
    if "open" in cmd:
        if "chrome" in cmd:
            return open_app("chrome")
        if "vs code" in cmd or "code" in cmd:
            return open_app("vscode")
        if "youtube" in cmd:
            return open_app("youtube")
        return "Which app should I open?"

    # Direct App Commands
    if "vs code" in cmd or "code" in cmd:
        return open_app("vscode")

    if "chrome" in cmd:
        return open_app("chrome")

    # Close Apps
    if "close" in cmd:
        if "chrome" in cmd:
            return close_app("chrome")
        if "vs code" in cmd or "code" in cmd:
            return close_app("vscode")
        return "Which app should I close?"

    # Search
    if "search" in cmd:
        query = extract_query(cmd, "search")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching {query}"

    # Wikipedia
    if any(x in cmd for x in ["who", "what", "tell me about"]):
        query = re.sub(r"(who|what|tell me about)", "", cmd).strip()
        return wikipedia_search(query)

    # Exit
    if cmd in ["exit", "stop", "quit"]:
        return "exit"

    return "Sorry, I didn't understand."


# ---------------------------
# Voice Listener
# ---------------------------
def listen():
    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        path = tmp.name

    try:
        print("Listening...")
        audio = sd.rec(int(DEFAULT_RECORD_SECONDS * 44100), samplerate=44100, channels=1)
        sd.wait()
        sf.write(path, audio, 44100)

        with sr.AudioFile(path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        print("You:", text)
        return text

    except sr.UnknownValueError:
        return None
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        if os.path.exists(path):
            os.remove(path)


# ---------------------------
# Main Loop
# ---------------------------
def main():
    speak("Assistant started. Listening...")

    while True:
        command = listen()

        if not command:
            continue

        response = process_command(command)

        if response == "exit":
            speak("Goodbye!")
            break

        speak(response)


# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    main()