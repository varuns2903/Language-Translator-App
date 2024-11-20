from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import googletrans
from googletrans import Translator
from gtts import gTTS
import pygame
import speech_recognition as sr
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Language Translator")
root.geometry("1000x600")
root.resizable(False, False)

frame = Frame(root, width=1000, height=600, relief=RIDGE, borderwidth=5, bg="#F7DC6F")
frame.place(x=0, y=0)

Label(
    root,
    text="LANGUAGE TRANSLATOR",
    font=("Times New Roman", 30),
    fg="black",
    bg="#F7DC6F",
).pack(pady=20)

try:
    pic_speak = Image.open("speak.png").resize((100, 50))
    image_speak = ImageTk.PhotoImage(pic_speak)

    pic_voice = Image.open("voice.jpg").resize((100, 50))
    image_voice = ImageTk.PhotoImage(pic_voice)

    pic_arrow = Image.open("arrow.jpg").resize((140, 100))
    image_arrow = ImageTk.PhotoImage(pic_arrow)
except FileNotFoundError as e:
    messagebox.showerror("Error", f"Missing file: {e.filename}")
    root.destroy()

Label(image=image_arrow, borderwidth=0).place(x=435, y=250)

def translate():
    input_text = text_entry_input.get("1.0", "end-1c")
    target_language = language_selector.get()

    if not input_text.strip():
        messagebox.showerror("Language Translator", "Enter the text to translate")
    else:
        text_entry_output.delete("1.0", "end")
        try:
            translator = Translator()
            translated = translator.translate(input_text, dest=target_language)
            text_entry_output.insert("end", translated.text)
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")

def clear():
    text_entry_input.delete("1.0", "end")
    text_entry_output.delete("1.0", "end")

def speak():
    text_to_speak = text_entry_output.get("1.0", "end-1c")
    if not text_to_speak.strip():
        messagebox.showerror("Error", "No text to speak!")
    else:
        try:
            speech = gTTS(text=text_to_speak)
            speech.save("data.mp3")
            
            pygame.mixer.init()
            pygame.mixer.music.load("data.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"Speech conversion failed: {e}")

def voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            messagebox.showinfo("Listening", "Please speak now...")
            audio = recognizer.listen(source)
            recognized_text = recognizer.recognize_google(audio)
            text_entry_input.delete("1.0", "end")
            text_entry_input.insert("end", recognized_text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand your voice")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Speech Recognition Error: {e}")

auto_detect = tk.StringVar()
auto_detect_combobox = ttk.Combobox(
    frame, width=27, textvariable=auto_detect, state="readonly", font=("verdana", 12, "bold")
)
auto_detect_combobox["values"] = ("Auto Detect",)
auto_detect_combobox.place(x=50, y=100)
auto_detect_combobox.current(0)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

selected_language = tk.StringVar()
language_selector = ttk.Combobox(
    frame, values=language_list, width=27, textvariable=selected_language, state="readonly", font=("verdana", 12, "bold")
)
language_selector.place(x=620, y=100)
language_selector.current(0)

text_entry_input = Text(
    frame, width=30, height=10, borderwidth=5, relief=RIDGE, font=("verdana", 15)
)
text_entry_input.place(x=10, y=150)

text_entry_output = Text(
    frame, borderwidth=5, height=10, width=30, relief=RIDGE, font=("verdana", 15)
)
text_entry_output.place(x=575, y=150)

btn_translate = Button(
    frame,
    command=translate,
    text="Translate",
    relief=RAISED,
    borderwidth=2,
    font=("Times New Roman", 12),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
    height=2,
    width=15,
)
btn_translate.place(x=135, y=470)

btn_clear = Button(
    frame,
    command=clear,
    text="Clear",
    relief=RAISED,
    borderwidth=2,
    font=("Times New Roman", 12),
    bg="#248aa2",
    fg="white",
    cursor="hand2",
    height=2,
    width=15,
)
btn_clear.place(x=680, y=470)

btn_speak = Button(
    frame, command=speak, image=image_voice, cursor="hand2", borderwidth=0, relief=FLAT
)
btn_speak.place(x=530, y=470)

btn_voice = Button(
    frame, command=voice, image=image_speak, cursor="hand2", borderwidth=0, relief=FLAT
)
btn_voice.place(x=350, y=470)

root.mainloop()
