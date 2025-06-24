# Your-Own-Jarvis

# 🎙️ Jarvis - Your Personal Voice Assistant

**Jarvis** is a smart voice-controlled assistant built using Python. It listens to your voice commands and performs various helpful tasks like searching Wikipedia, playing music, opening apps, sending emails, and more — just like your own desktop Jarvis!

---

## ✨ Features

- 🧠 Search and read summaries from Wikipedia  
- 🎵 Play music from your local folder  
- 🌐 Open websites like Google, YouTube, Stack Overflow  
- ⏰ Tell the current time  
- 📧 Send emails using your voice  
- 🤪 Tell jokes and fun facts  
- 🗣️ Personalized greeting based on time of day

---

## 🛠️ Tech Stack & Libraries

- **Python 3.8+**
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – Text-to-speech engine  
- [`speechrecognition`](https://pypi.org/project/SpeechRecognition/) – For voice input  
- [`wikipedia`](https://pypi.org/project/wikipedia/) – Fetch summaries from Wikipedia  
- Built-in modules: `datetime`, `os`, `webbrowser`, `smtplib`

---

## 🚀 Getting Started

Install dependencies 
```bash
pip install -r requirements.txt
```
⚠️ For this project, I installed packages globally without using a virtual environment.
However, using a virtual environment (venv) is highly recommended for better project isolation and compatibility.

Using Virtual Env-
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt

```
Run Jarvis
```bash
python main.py
```

