from screenShot.screenshot import ScreenShot

"""
ScreenShotクラスと、各FunctionクラスのIF（インターフェース）クラス
各Functionクラスの改修の影響を抑えるために作成
（を考えていたが、現在のところそこまで価値がないように思えている）
"""

class Driver():
    def __init__(self):
        pass

    def invoke(self, func_name):
        func_name.do()