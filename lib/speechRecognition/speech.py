import sys
sys.path.append('../../')

import speech_recognition as sr
from lib.util import _logger_setup
from lib.driver import Driver
import config
import logging

class Error(Exception):
    pass

class speechRecognition():

    def __init__(self, func):
        self.function = 'ScreenShot'
        #self.function = config.FUNC_NAME
        self.logger = _logger_setup(logging.DEBUG)
        #self.mic_name = config.MIC_NAME
        self.mic_name = 'Built-in Microphone'
        self.recognizer = sr.Recognizer()
        self.driver = Driver()
        self.mic = sr.Microphone(device_index=(self._ret_mic_index()))

    def run(self):
        # obtain audio from the microphone
        while True:
           self.logger.info("Start Speech Recognition")
           with self.mic as source:
              self.recognizer.adjust_for_ambient_noise(source, duration=0.5) # ノイズ軽減 @https://realpython.com/python-speech-recognition/#the-effect-of-noise-on-speech-recognition
              audio = self.recognizer.listen(source)
           try:
              # 'stop'を認識したら終了する
              word = self.recognizer.recognize_sphinx(audio)
              if word.lower() in ['stop', 'stop it']:
                  self.logger.debug("Speech Recognition is over.")
                  break
              
              # ./lib/python3.6/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict
              # 上記ファイルに 'kawaii' を追加したが認識してくれない。そのため、かわいい を発した際に Sphinx が認識したワードを用いる
              elif word.lower() in ['kawaii', 'corey', 'hawaii']:
                  self.logger.debug("The function activate...")
                  # configで設定した実行機能
                  self.driver.invoke(self.function)
              
              else:
                  self.logger.debug("Sphinx thinks you said " + word)
                  self.logger.debug("Still continue")
           
           except sr.UnknownValueError:
              self.logger.error("Sphinx could not understand audio")
           except sr.RequestError as e:
              self.logger.error("Sphinx error; {0}".format(e))

    """ユーザが利用するマイクのインデックスを返却する"""
    def _ret_mic_index(self):
        print(sr.Microphone.list_microphone_names())
        try:
           return sr.Microphone.list_microphone_names().index(self.mic_name)
        except Exception as e:
           raise Error('configにて選択したマイクは存在しません。 Key:MIC_NAME')
