# Import necessary libraries

import pyttsx3
# Library for text-to-speech conversion

import datetime
# Library for handling date and time

import speech_recognition as sr
# Library for speech recognition

import wikipedia
# Library for fetching information from Wikipedia

import re
# Regular expression library for text processing

import webbrowser
# Library for opening web browser

from tkinter import *
# Library for GUI

import customtkinter
# Custom theme library for tkinter

import tkinter as tk
# Additional tkinter functionality


# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

# Function to define the main functionality of the program
def main():
    # Function to speak a given text
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # Function to provide a time-based greeting
    def greeting():
        hour = int(datetime.datetime.now().hour)
        if 5 <= hour < 12:
            speak("Good Morning Sir")
        elif 12 <= hour < 17:
            speak("Good Afternoon Sir")
        elif 17 <= hour < 22:
            speak("Good Evening Sir")
        else:
            speak("Hello Sir")

        speak("This is RASS. How may I assist you ")

    # Function to capture user's voice command
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing Command......")
            query = r.recognize_google(audio, language='eng-in')
            print("User said: ", query)

        except Exception as e:
            print("Sorry I can't Understand! Can you say that again please?")
            return "None"
        return query

    # Function to fetch and speak a summary from Wikipedia
    def wikisummary(query):
        num_sentences = 2

        # Get the summary
        summary = wikipedia.summary(query)

        # Split the summary into sentences
        sentences = re.split('(?<=[.!?]) +', summary)

        # Take the first num_sentences sentences
        results = ' '.join(sentences[:num_sentences])
        speak("According to Wikipedia")
        print(results)
        speak(results)

    # Placeholder function for sending emails
    def sendEmail(to, content):
        pass

    # Main execution starts here
    if __name__ == "__main__":
        greeting()

        # while True:  # Uncomment this line if you want the program to continuously listen
        if 1:  # This is equivalent to 'while True' for now, change it based on your requirements
            query = takeCommand().lower()

            if "wikipedia" in query:
                speak("Searching Wikipedia....")
                query = query.replace("wikipedia", " ")
                wikisummary(query)

            elif "open youtube" in query:
                speak("Opening Youtube")
                webbrowser.open("youtube.com")

            elif "open cuims" in query:
                speak("Opening CUIMS")
                webbrowser.open("https://uims.cuchd.in")

            elif "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"the time is {strTime}")

            elif "repeat after me" in query:
                query = query.replace("repeat after me", " ")
                speak(query)

# Set appearance mode and default color theme for the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window
root = customtkinter.CTk()
root.title('RASS')
root.geometry('700x500')
photo = PhotoImage(file="ezgif.com-resize.png")

# Create a button to activate RASS
my_button = customtkinter.CTkButton(root, text="ACTIVATE RASS",
                                    height=120, width=250, font=("Helvetica", 30, 'bold'),
                                    fg_color="#00FFFF", text_color="black",
                                    command=main, image=photo,
                                    corner_radius=50,
                                    hover_color='green', border_width=5, border_color="green"
                                    )
my_button.pack(pady=130)

# Create an exit button
exit_btn = customtkinter.CTkButton(root, text="EXIT", height=100, width=90,
                                   font=("Helvetica", 18, 'bold'),
                                   fg_color="white", text_color="black",
                                   command=root.quit, hover_color="#D2042D")
exit_btn.pack(padx=100, pady=50)

# Start the main loop for the GUI
root.mainloop()
