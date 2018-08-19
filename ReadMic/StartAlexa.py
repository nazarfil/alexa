from ReadMic.audio_to_text import Listener
from ReadMic.text_to_speech import Speaker
from ReadMic.commands import available_commands

import time
class Alexa(object):
    def __init__(self, loud, engine, owner=None):
        self.owner=owner
        #setting up listener and recognition
        self.listener = Listener()
        self.listener.set_up(engine)

        #setting up speach answer
        self.speaker = Speaker(loud)

        #setting up commands
        self.cmd = available_commands

    def run(self):
        # recognize speech using Google Speech Recognition
        start_time = time.time()
        while True:
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`

                audio = self.listener.get_audio()
                text_is = self.listener.recognize_audio(audio)
                answer = ""
                for command in self.cmd:
                    if command.name in text_is:
                        for val in command.values:
                            if val in text_is:
                                command.changeStatus(val)
                                answer = command.answerCmd(val)

                greet, greet_text = self.greetMyself(time.time() - start_time, text_is)
                answer_text =""
                if(greet):
                    answer_text = greet_text + self.owner

                self.speaker.say(answer_text + answer)


            except self.listener.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except self.listener.RequestError as e:
                print("Could not request results from Speech Recognition service; {0}".format(e))

    def greetMyself(self, dtime, text):
        list_greets = ["good morning", "hello", "hi","good afternoon"]
        if dtime > 300:
            return (True, "Hi")
        for item in list_greets:
            if item in text:
                return (True,item)
        return False, "No"



alexa = Alexa(True, "google", "Nazar")
alexa.run()