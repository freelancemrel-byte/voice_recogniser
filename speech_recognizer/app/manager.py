class CommandManager:
    def __init__(self, command_list):
        self.command_list = command_list

    def get_command(self, input_text):
        command_key = self.get_command_key(input_text)
        if command_key is None:
            return None
        return self.command_list.get(command_key)
    def get_command_key(self, input_text):
        for key in self.command_list.keys():
            if key in input_text.lower():
                return key
        return None