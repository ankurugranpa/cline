# line notify for cli
## SetUp
LINE_NOTIFY_APIという環境変数を設定する必要があります。
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
-m は必須オプションです
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
