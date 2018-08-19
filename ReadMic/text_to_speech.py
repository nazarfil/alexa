import os
import pyttsx3

class Speaker(object):
    def __init__(self, loud):
        self.loud = loud
        self.loud_engine = pyttsx3.init()

    def say(self, text_to_say):
        if (self.loud):
            self.loud_engine.say(text_to_say)
            self.loud_engine.runAndWait()
        else:
            print("SILENT MODE : "  + text_to_say)