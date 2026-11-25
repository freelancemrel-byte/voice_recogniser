
from datetime import datetime

from app.speaker import Speaker
import webbrowser

def speak_time():
    time_now = datetime.now().strftime("%I:%M %p")
    text=f"The current time is {time_now}"
    Speaker.speak(text)

def open_youtube():
    webbrowser.open("https://www.youtube.com")