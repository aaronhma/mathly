# Define a standard message here
class StandardMessage:
    def __init__(self):
        self.std_msg = True
    
    def read_message(self, file):
        with open(file, "r") as file:
            file.read()