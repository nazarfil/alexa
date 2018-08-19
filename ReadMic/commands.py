class Command(object):
    def __init__(self, name):
        self.name = name

class BinaryCommand(Command):
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.status = "off"
        self.values = ["off", "on"]

    def changeStatus(self, cmd):
        if(cmd == "on"):
            self.value = 1
            self.status = "on"
        else:
            self.value = 0
            self.status = "off"

    def answerCmd(self, cmd):
        answers = {
            "on" : "Turning on the ",
            "off" : "Turning off the "
        }
        return answers[cmd]+self.name+"!"


lights = BinaryCommand("lights")
available_commands = [
    lights
]