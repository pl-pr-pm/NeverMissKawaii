import sys
sys.path.append('../../')
print(sys.path)

"""
ScreenShotクラスと、各FunctionクラスのIF（インターフェース）クラス
各Functionクラスの改修の影響を抑えるために作成
（を考えていたが、現在のところそこまで価値がないように思えている）
"""

class Driver():
    def __init__(self):
        pass

"""
クロージャを利用（使ってみたかっただけ）
"""
    def invoke(self, func):
        def inner():
            func.do()
        return inner