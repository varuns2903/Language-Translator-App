# Language Translator App

This is a Python-based Language Translator application that uses the Google Translate API for text translation, Google Text-to-Speech (gTTS) for speaking translations aloud, and speech recognition for converting spoken words to text. The app features a simple graphical user interface (GUI) built with Tkinter.

## Features

- **Text Translation**: Translate text from any language to a selected target language.
- **Text-to-Speech**: Listen to the translated text with the built-in speech synthesizer.
- **Voice Input**: Speak into the microphone and have the app transcribe your speech to text for translation.
- **Clear Button**: Clears both input and output text fields.
- **Auto-Detect Input Language**: Automatically detects the language of the input text.

## Requirements

Before running the app, you need to install the following dependencies:

- `googletrans==4.0.0-rc1` - for translation
- `gTTS==2.2.3` - for text-to-speech
- `pygame==2.5.4` - for playing audio
- `SpeechRecognition==3.8.1` - for voice input
- `Pillow==9.6.1` - for image processing

You can install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Setup Instructions
Clone this repository to your local machine:
```bash
git clone https://github.com/varuns2903/Language-Translator-App.git
```
Navigate into the project directory:
```bash
cd Language-Translator-App
```
Install required dependencies:
```bash
pip install -r requirements.txt
```
Place the required images (speak.png, voice.jpg, and arrow.jpg) in the project directory. These images are used for the UI buttons, so make sure they are available.

Run the app:
```bash
python translator_app.py
```
