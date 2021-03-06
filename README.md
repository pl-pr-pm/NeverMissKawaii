# NeverMissKawaii

NeverMissKawaii （以下 NMK）は、「可愛いと思ったこの一瞬を永遠に」 を実現するアプリケーションです。  
NMK の起動中、ユーザーの「かわいい」というワードを検知し、アクティブなブラウザのスクリーンショットを実行してくれます。  
NMK によって以下の出来事が解消されます。

- Youtube でかわいいと思った場面を見返したいが、どのあたりか忘れてしまった
- 生放送閲覧中に可愛すぎてスクリーンショットを忘れてしまった、アーカイブされていないので確認ができない
  NMK はユーザーの発する「かわいい」というワードを検知するため、かわいいの保存を逃すことがありません。  
  実行速度を最大まで早くするために、一般的にボトルネックとなるネットワーク IO を排除しオフラインでの音声認識実行を実現  
  NMS を利用し、一瞬を永遠に。

### 操作

_python3.6.8 で動作確認済みです_

```
cd neverMissKawaii/
python3.6.8 main.py
```

- 「かわいい」と発音すると、アクティブなスクリーンのスクショが実行されます。
  デフォルトの保存先は、neverMissKawaii/ です。

- 「stop」と発音すると、アプリケーションが終了します。

_注意点_
「かわいい」という発音には少し気をつける必要があります。  
「かわいいー」ではなく、  
「っかわいい」と発音してください。アクセントは「っか」の部分です。  
そのようにすることで、NMK が かわいい を捉えてくれます。

### 辞書追加

pronounciation-dictionary.dict  
上記辞書ファイルを speech_recognition/pocketsphinx-data/en-US/ 配下に追加することで、「かわいい」を認識します

### マイク変更

conig.py にて MIC*NAME= の値を変更します  
MIC_NAME は、NMK を実行すると、標準出力でターミナルに表示されます  
\_bluetooth でのマイクの場合、有線のマイクより遅延が発生します*

### デモ

![NMK_resize](https://user-images.githubusercontent.com/59119963/159640702-0b08c68d-a61e-4f4a-9e44-9489636249cc.gif)

### 仕組み

1. SpeechRecognition(https://pypi.org/project/SpeechRecognition/) を利用し、音声識別を実施  
内部の音声エンジンはオフラインで実施したいためCMU Sphinx(https://cmusphinx.github.io/wiki/)を利用

2. SpeechRecognitionで識別した音声に応じてアクションを実施  
「かわいい」であればスクリーンショットを実施
「stop」であればアプリケーション終了とする
