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
            'friendId': 3269308288,
            'msg': ''
        }

        response = requests.post(url, headers=headers, json=data)

        url = "http://modsgs.sandboxol.com/friend/api/v1/friends/requests/approve-all"

        headers = {
            'userId': '3269308288',
            'Access-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMjY5MzA4Mjg4IiwiaWF0IjoxNzIyMzYzNjE4LCJzdWIiOiIyMDI0MDczMCAxODIwMTg3MzMiLCJpc3MiOiJTYW5kYm94LVNlY3VyaXR5LUJhc2ljIiwiZXhwIjoxNzIyOTY4NDE4fQ.UwxDUuZ6JehFlpajI7NoVM78O9MxVP-ec5-6ikiM3SM',
            'packageName': 'amosCraft',
            'User-Agent': 'okhttp/3.12.1'
        }

        response = requests.post(url, headers=headers)

        url = "http://modsgs.sandboxol.com/friend/api/v1/popularity?friendId=3269308288"

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

        url = "https://gw.sandboxol.com/friend/api/v1/friends?friendId=3269308288"

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
