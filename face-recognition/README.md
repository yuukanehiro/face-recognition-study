# face-recognition-study

# face-recognition

## 概要
顔認識のサンプルコードです。
OpenCVとdlibを使用して、顔の検出と認識を行います。

## 環境構築

```bash
brew install pyenv
```

```bash
% vi ~/.zshrc

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

```bash
source ~/.zshrc
```
```bash
pyenv install --list
```
```bash
pyenv install 3.10.14
```
```bash
pyenv local 3.10.14
```

```bash
% python -V
Python 3.10.14
```

## 仮想環境の作成と依存関係のインストール

```bash
python -m venv venv
source venv/bin/activate
```

```bash
pip install --upgrade pip
```

```bash
brew install cmake
brew install boost
```

```bash
pip install opencv-python face_recognition
```


face-recognition/known_faces
配下に顔写真のjpgファイルを配置します。

## スクリプト実行
```bash
python face_app.py
```

## venvの終了
```bash
deactivate
```

## 注意点
- 顔写真は、`face-recognition/known_faces` ディレクトリに配置してください。
- 顔写真のファイル名は、認識時の名前として使用されます。
- 顔写真は、正面を向いているものが望ましいです。
- 顔写真の解像度は、128x128ピクセル程度が推奨されます。
- 顔写真の枚数は、認識精度に影響します。できるだけ多くの顔写真を用意してください。

## ToDo
- 顔認識の精度向上のために、顔写真の前処理を行う。
- 複数の顔写真を登録できるようにする
- 顔認識の結果をGUIで表示する
- 顔認識の結果をログに記録する
- 顔認識の結果をデータベースに保存する
- 顔認識の結果をWebアプリケーションで表示する
- 顔認識の結果をAPIで提供する
- 顔認識の結果をリアルタイムで表示する
- FIDO 認証に対応する

## リンク

* [【AI×Raspberry Pi】手書き数字をリアルタイム認識するシステムを作ってみた【ColabでAI学習 → Raspberry Piで実行】](https://www.youtube.com/watch?v=yKd6gv3TAFo)
