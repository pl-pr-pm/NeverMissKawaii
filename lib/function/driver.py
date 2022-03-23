import sys
sys.path.append('../../')

"""
ScreenShotクラスと、各FunctionクラスのIF（インターフェース）クラス
各Functionクラスの改修の影響を抑えるために作成
"""

class Driver():
    def __init__(self):
        pass

    def invoke(self, func):
        def inner():
            func.do()
        return inner