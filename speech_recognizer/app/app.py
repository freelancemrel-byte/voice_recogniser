
from app.commands import COMMANDS
from app.manager import CommandManager
from app.speaker import Speaker
from app.voice_listener import VoiceListener


class App:
    def __init__(self):
        self.run()

    def run(self):
        speaker = Speaker()
        command = VoiceListener().listen()
        command_manager = CommandManager(COMMANDS)
        action = command_manager.get_command(command)
        if action:
            action()
            speaker.run()
        else:
            speaker.speak("Sorry, I didn't understand that command.")
            speaker.run()