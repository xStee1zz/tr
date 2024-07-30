import random
import threading

import requests

with open('bot.txt', 'r') as file:
    bots = file.readlines()

def like():
    while True:
        bot = random.choice(bots).strip()
        bot_id, bot_token = bot.split(':')

        url = "https://gw.sandboxol.com/friend/api/v1/friends"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        data = {
            'friendId': 65980143,
            'msg': ''
        }

        response = requests.post(url, headers=headers, json=data)

        url = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/approve-all"

        headers = {
            'userId': '65980143',
            'Access-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2NTk4MDE0MyIsImlhdCI6MTcyMjM2MjY2NSwic3ViIjoiMjAyNDA3MzAgMTgwNDI1ODI4IiwiaXNzIjoiU2FuZGJveC1TZWN1cml0eS1CYXNpYyIsImV4cCI6MTcyMjk2NzQ2NX0.8f4OFu535pHBtW_nYH1wXCA6GAct_554FwX8Ub3pxxQ',
            'packageName': 'amosCraft',
            'User-Agent': 'okhttp/3.12.1'
        }

        response = requests.post(url, headers=headers)

        url = "http://modsgs.sandboxol.com/friend/api/v1/popularity?friendId=65980143"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'packageName': 'amosCraft',
            'User-Agent': 'okhttp/3.12.1'
        }

        response = requests.post(url, headers=headers).json()
        message = response['message']

        if message == "SUCCESS":
            print(f"\033[1m\033[32m{response['data']}\033[0m")
        else:
            print(f"\033[1m\033[31m{message}\033[0m")

        url = "https://gw.sandboxol.com/friend/api/v1/friends?friendId=65980143"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'User-Agent': 'okhttp/3.12.1'
        }

        response = requests.delete(url, headers=headers)

threads = []
for _ in range(3):
    t = threading.Thread(target=like)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
