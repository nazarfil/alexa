import speech_recognition as sr
# obtain audio from the microphone
class Listener(sr.Recognizer):

    def set_up(self, engine):
        print("SetUp")
        self.micro = sr.Microphone()
        self.engine = engine
        self.switcher = {
            "google": self.recognize_google,
            "sphinx":self.recognize_sphinx
        }

    def get_audio(self):
        print("Say something!")
        with sr.Microphone() as source:
            audio = self.listen(source)
        return audio

    def recognize_audio(self, audio):
        try:
            text = self.switcher[self.engine](audio)
        except sr.UnknownValueError:
            text = "Unkown"

        print("Speech Recognition thinks you said " + text)
        return text