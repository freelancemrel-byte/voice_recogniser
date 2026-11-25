import pyttsx3 as tts
class Speaker:
    def __init__(self):
        self.engine = tts.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

    def speak(self, text):
        self.engine.say(text)
    def run(self):
        self.engine.runAndWait()