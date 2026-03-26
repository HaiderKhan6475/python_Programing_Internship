\# 🎙️ Voice Assistant (Python)



A smart desktop voice assistant built with Python that can listen to your voice commands and perform tasks like opening applications, searching the web, telling time/date, and fetching information from Wikipedia.



\---



\## 🚀 Features



\* 🎤 Voice command recognition

\* 🗣️ Text-to-Speech response

\* 🌐 Open websites (Google, YouTube)

\* 💻 Open desktop apps (Chrome, VS Code)

\* ❌ Close opened applications

\* 🔍 Google search via voice

\* 📚 Wikipedia search

\* ⏰ Tell current time and date

\* 💬 Basic conversation support



\---



\## 🛠️ Tech Stack



\* Python

\* SpeechRecognition

\* sounddevice

\* soundfile

\* pyttsx3

\* wikipedia

\* subprocess / os / webbrowser



\---



\## 📁 Project Structure



```

voice-assistant/

│── main.py        # Main assistant code

│── README.md      # Project documentation

```



\---



\## ⚙️ Installation



\### 1. Clone Repository



```bash

git clone https://github.com/your-username/voice-assistant.git

cd voice-assistant

```



\### 2. Create Virtual Environment (Recommended)



```bash

python -m venv venv

venv\\Scripts\\activate

```



\### 3. Install Dependencies



```bash

pip install speechrecognition sounddevice soundfile pyttsx3 wikipedia

```



\---



\## ▶️ Usage



Run the assistant:



```bash

python main.py

```



Speak commands like:



\* "Open Chrome"

\* "Open VS Code"

\* "Search Python tutorials"

\* "What is Artificial Intelligence"

\* "What time is it"

\* "Close Chrome"

\* "Stop"



\---



\## 🧠 How It Works



1\. Records audio using microphone

2\. Converts speech to text using Google Speech API

3\. Processes command using rule-based logic

4\. Executes action (open app, search, etc.)

5\. Responds using text-to-speech



\---



\## ⚡ Example Commands



| Command        | Action            |

| -------------- | ----------------- |

| Open Chrome    | Launch browser    |

| VS Code        | Open VS Code      |

| Search AI      | Google search     |

| What is Python | Wikipedia summary |

| Time           | Current time      |

| Exit           | Stop assistant    |



\---



\## 🔧 Configuration



Update paths in `main.py`:



```python

CHROME\_PATH = "your chrome path"

VSCODE\_PATH = "your vscode path"

```



\---



\## 🚧 Future Improvements



\* 🤖 AI/NLP-based intent detection

\* 🎯 More accurate speech recognition (Whisper/Vosk)

\* 📱 WhatsApp \& Email automation

\* 🖥️ System control (shutdown, restart)

\* 🌍 Multi-language support



\---



\## 🙌 Contributing



Feel free to fork this repo and improve the assistant!



\---



\## 📜 License



This project is open-source and available under the MIT License.



\---



\## 👨‍💻 Author



\*\*Haider Khan\*\*

Python Developer | AI Enthusiast 🚀



\---



