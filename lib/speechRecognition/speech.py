import sys
sys.path.append('../../')

import speech_recognition as sr
from lib.util import _logger_setup, _match_word
from lib.function.driver import Driver
from lib.function.screenShot.screencapture import ScreenShot
import config
import logging

class Error(Exception):
    pass

"""
speech_recognition を利用して、音声認識機能を提供。
音声によってスクリーンショットなどの機能の実行が可能。
"""
class speechRecognition():

    def __init__(self, func):
        self.function = func
        self.logger = _logger_setup(logging.DEBUG)
        self.mic_name = config.MIC_NAME
        self.recognizer = sr.Recognizer()
        self._tune_recognizer_parameter()
        self.driver = Driver()
        self.mic = sr.Microphone(device_index=(self._ret_mic_index()), sample_rate=15000, chunk_size=256)

    def run(self):
        # obtain audio from the microphone
        while True:
           self.logger.info("Start Speech Recognition")
           with self.mic as source:
              self.recognizer.adjust_for_ambient_noise(source, duration=0.5) # ノイズ軽減 @https://realpython.com/python-speech-recognition/#the-effect-of-noise-on-speech-recognition
              audio = self.recognizer.listen(source)
           
           try:
              word = self.recognizer.recognize_sphinx(audio)

              # ./lib/python3.6/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict
              # 上記ファイルに 'kawaii' を追加したが認識してくれない。そのため、かわいい を発した際に Sphinx が認識したワードを用いる
              if _match_word(patterns=[r'wai', r'kawai', r'corey', r'hawaii'], word=word):
                  self.logger.debug("The function activate...")
                  # configで設定した実行機能
                  self.driver.invoke(self.function)
               
               # 'stop'を認識したら終了する
              elif _match_word(patterns=[r'stop'], word=word):
                  self.logger.debug("Speech Recognition is over.")
                  break
              
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
    
    """ recognizerのパラメタをチューニングする"""
    def _tune_recognizer_parameter(self):
        # サウンドのエネルギーレベルのしきい値を表します。このしきい値を下回る値は無音と見なされ、このしきい値を超える値は音声と見なされます。
        # デフォルトは300だが、ノイズと間違えないように大きい声で検出するように値を引き上げる
        self.recognizer.energy_threshold = 1000
        # フレーズの終わりとして登録される無音の最小の長さ（秒単位）
        self.pause_threshold = 0.001