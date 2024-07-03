# Line Notify for ClI
[Line Notify](https://notify-bot.line.me/ja/)をcli上からいい感じに使えるようにする cli tool


## Requirement
`python >= 3.8`\
` poetry` or` pip`

※ poetryがおすすめ
## SetUp
### install
```
git clone https://github.com/ankurugranpa/cline.git
cd cline
```
- 依存関係のインストール
```
poetry install 
```
or
```
pip install -r requirement.txt
```

### 環境変数の設定
LINE_NOTIFY_APIという環境変数を設定する必要があります。\
※APIキーの取得をしていない方は[こちら](https://notify-bot.line.me/ja/)から取得してください
- linux系のosの場合
```
export LINE_NOTIFY_API="yor_api_token" 
```
または
```shell
cp .env.exsample .env 
vim .env #.envを好きなエディタで開きtokenを記述
```

## Usage
引き数に[-i, --message] か [-s, --status] か [-c, --check]のどれか一つは取らなければなりません
```
usage: cline.py [-h] -m MESSAGE [-i IMAGE] [-s]

line notifyを使用したcliからlineへの通知ライブラリ

options:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        メッセージの内容
  -i IMAGE, --image IMAGE
                        画像ファイルパス
  -s, --status          ステータスコードの表示
```

## Warning
Line Notify APIはレート制限が設けられているので注意してください\
[詳細](https://notify-bot.line.me/doc/ja/)
