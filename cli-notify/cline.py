import os
import requests
import argparse

from dotenv import load_dotenv

class cline():
    def __init__(self, line_api_token) -> None:
        self.__line_notify_api = 'https://notify-api.line.me/api/notify'
        self.__headers = {'Authorization': f'Bearer {line_api_token}'}
        self.__files = None
        self.__message = None

    def set_message(self, line_message):
        self.__message = {'message': f'message: {line_message}'}

    def set_image(self, image_path):
        self.files = {"imageFile":open(image_path,'rb')}

    def send(self): 
        requests.post(self.__line_notify_api, headers = self.__headers, data = self.__message, files=self.__files)



def main():
    load_dotenv()
    LINE_NOTIFY_API = os.getenv("LINE_NOTIFY_API")

    parser = argparse.ArgumentParser(description='line notifyを使用したcliからlineへの通知ライブラリ')
    parser.add_argument('message', help='メッセージの内容') 
    parser.add_argument('-i', '--image', help='画像ファイルパス')    


    args = parser.parse_args()
    test = cline(LINE_NOTIFY_API)
    # print(args.image)
    test.set_message(args.message)
    test.send()

if __name__ == "__main__":
    main()
