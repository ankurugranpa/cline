import os
import argparse
import datetime
from pathlib import Path
from typing import Optional, Dict, BinaryIO
import sys

import requests
from requests.models import CaseInsensitiveDict
from dotenv import load_dotenv

class Cline():


    def __init__(self, line_api_token) -> None:
        self.__line_notify_api = 'https://notify-api.line.me/api/notify'
        self.__headers = {'Authorization': f'Bearer {line_api_token}'}
        self.__files: Optional[Dict[str, BinaryIO]] = None
        # self.__files = None
        self.__message: Optional[Dict[str, str]] = None
        self.__response_headers: Optional[CaseInsensitiveDict] = None
        self.__status_code = None
        self.check()


    def set_message(self, line_message:str):
        self.__message = {'message': f'\n{line_message}'}


    def set_image(self, image_path:Path):
        self.__files = {"imageFile":open(image_path,'rb')}


    def send(self) -> CaseInsensitiveDict: 
        if (self.__message == None and self.__files == None):
            return self.check()
        else:
            res = requests.post(self.__line_notify_api, headers = self.__headers, data = self.__message, files=self.__files)
            self.__response_headers = res.headers
            self.status_code(res.json())
            return self.__response_headers
        

    def check(self) -> CaseInsensitiveDict:
        status_api = "https://notify-api.line.me/api/status"
        status = requests.get(status_api, headers=self.__headers)
        self.__response_headers = status.headers
        self.__status_code = status.json()
        self.status_code(status.json())
        return self.__response_headers

    def status_code(self, code:dict):
        if(code["status"] != 200):
            print(f"ERROR: {code['message']}")

    def show_status_code(self):
        print(self.__status_code)


    def show_status(self):
        header =  self.__response_headers
        print("<=== Line Notify Status ===>")
        print("## Yor Status ##")
        print(f"残りの送信可能回数: {header['X-RateLimit-Remaining']}")
        print(f"残りの画像送信可能回数: {header['X-RateLimit-ImageRemaining']}")
        print("")
        print("## Rate Limit ##")
        print(f"1時間に送信可能な画像枚数上限: {header['X-RateLimit-ImageLimit']}")
        print(f"1時間に送信可能なメッセージ上限: {header['X-RateLimit-Limit']}")
        print(f"次の制限のリセット日時: {datetime.datetime.fromtimestamp(int(header['X-RateLimit-Reset']))}")
        



def main():
    load_dotenv()
    LINE_NOTIFY_API = os.getenv("LINE_NOTIFY_API")
    if(LINE_NOTIFY_API == None or LINE_NOTIFY_API == "your_line_notify_api_key"): 
       print("Error: API KEYが見つかりません。適切に設定してください\nSee:'https://github.com/ankurugranpa/cline?tab=readme-ov-file'",
             file=sys.stderr)
       sys.exit(1)


    # set arg
    parser = argparse.ArgumentParser(description='line notifyを使用したcliからlineへの通知ライブラリ')
    parser.add_argument('-m', '--message', help='メッセージの内容') 
    parser.add_argument('-i', '--image', help='画像ファイルパス, 一枚ずつしか送れません')    
    parser.add_argument('-s', '--status', action='store_true',  help='ステータスコードの表示')    
    parser.add_argument('-c', '--check', action='store_true', help='tokenの確認')    

    args = parser.parse_args()

    message = Cline(LINE_NOTIFY_API)

    message.set_message(args.message)

    if not (args.message or args.status or args.check):
        parser.error("[-i, --message] or [-s, --status] or [-c, --check] のオプションが必要です")
    else:
        # send message logic
        if args.message != None:
            message.set_message(args.message)

            if args.image != None:
                message.set_image(args.image)

            message.send()

        elif args.image != None:
            parser.error("[-i, --image]オプションを使うには[--message]オプションが必須です")


        # option logic
        if args.status == True:
            message.show_status()

        if args.check == True:
            message.show_status_code()



if __name__ == "__main__":
    main()
