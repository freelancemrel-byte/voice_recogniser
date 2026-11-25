import speech_recognition as sr

class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None