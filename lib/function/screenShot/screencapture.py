import sys
sys.path.append('../../../')

from lib.util import _logger_setup, _get_now_str
import config
import logging
import subprocess
import os

"""
自作スクリーンショットクラス
ググるとpython でスクリーンショットのライブラリは以下三つがヒットした

- PIL https://github.com/python-pillow/Pillow
- pyscreeze https://github.com/asweigart/pyscreeze/tree/master/pyscreeze
- pyautogui

pyautogui は、内部で pyscreeze を利用し、 pyscreezeは、PIL を利用している。
PILは、 subprocess でscreenshotを実行している。その後、PILの関数を利用し、トリミングを行なっている。

NMKは、リアルタイムで早急なスクリーンショット実行が必要なため純粋なスクリーンショット機能を自作で作成する。
（とは言っても、subprocess で screencapture を実行するのみではあるが）
"""

class ScreenShot():
    
    logger = _logger_setup(logging.DEBUG)
    output_path = config.OUTPUT_PATH + _get_now_str() + '.jpg'
    
    """スクリーンショット実行"""
    @classmethod
    def do(cls):
        # -x → サウンドなし
        try:
           #subprocess.call(["screencapture", "-x", cls.output_path])
           subprocess.call(["screencapture", cls.output_path])
           cls.logger.debug('スクリーンショット取得完了。保存先：' + cls.output_path)
        
        except Exception as e:
           cls.logger.error('スクリーンショット取得に失敗しました')
           cls.logger.error(e)
           cls._delete()
    
    """作成ファイルを削除"""
    def _delete():
        os.unlink(cls.output_path)