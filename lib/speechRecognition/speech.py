import speech_recognition as sr
import logging

class speechRecognition():
    def __init__(self, func):
        # self.function = function
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        
    
    def run(self):
        # obtain audio from the microphone
        
        while True:
               
        with self.mic as source:
           print("Say something!")
           audio = self.recognizer.listen(source)

    # recognize speech using Sphinx
        try:
           print("Sphinx thinks you said " + self.recognizer.recognize_sphinx(audio))
        except sr.UnknownValueError:
           print("Sphinx could not understand audio")
        except sr.RequestError as e:
           print("Sphinx error; {0}".format(e))
   
   def __logger_setup(self):
          

