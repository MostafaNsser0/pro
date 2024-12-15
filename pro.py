import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = entry.get()
    if text.strip():
        tts = gTTS(text=text, lang='en')
        tts = gTTS(text=text, lang='ar')
        tts.save("speech.mp3")
        os.system("start speech.mp3")
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال نص للتحويل إلى صوت!")

def clear_text():
    entry.delete(0, tk.END)

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("تحويل النص إلى صوت")
window.geometry("600x400")
window.config(bg="#f0f0f0")

title_label = tk.Label(window, text="مشروع تحويل النص إلى صوت", font=("Arial", 20), bg="#f0f0f0")
title_label.pack(pady=20)

entry = tk.Entry(window, width=50, font=("Arial", 14))
entry.pack(pady=10)

btn_frame = tk.Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=20)

btn_play = tk.Button(btn_frame, text="تشغيل", font=("Arial", 15), bg="green", fg="white", command=play_text)
btn_play.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(btn_frame, text="مسح النص", font=("Arial", 15), bg="blue", fg="white", command=clear_text)
btn_clear.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(btn_frame, text="خروج", font=("Arial", 15), bg="red", fg="white", command=exit_app)
btn_exit.grid(row=0, column=2, padx=10)

window.mainloop()
