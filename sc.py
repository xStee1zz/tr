import random
import threading

import requests

with open('bot.txt', 'r') as file:
    bot_list = file.readlines()

with open('proxy.txt', 'r') as file:
    proxy_list = file.readlines()

def fspam():
    while True:
        bot = random.choice(bot_list).strip()
        bot_id, bot_token = bot.split(':')

        url = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'packageName': 'amosCraft',
            'User-Agent': 'okhttp/3.12.1'
        }

        proxies = {
            'http': random.choice(proxy_list).strip()
        }

        try:
            response = requests.delete(url, headers=headers, proxies=proxies)
        except:
            continue

        headers = {
            'userId': bot_id,
            'Access-Token': bot_token,
            'packageName': 'amosCraft',
            'appVersion': '5062',
            'userLanguage': 'ru_RU',
            'User-Agent': 'okhttp/3.12.1'
        }

        data = {
            'age': 200,
            'memberType': random.randint(1, 4),
            'ownerType': random.randint(1, 4)
        }

        proxies = {
            'http': random.choice(proxy_list).strip()
        }

        try:
            response = requests.post(url, headers=headers, json=data, proxies=proxies).json()
        except:
            continue

        print(response['message'])

threads = []
for _ in range(500):
    t = threading.Thread(target=fspam)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
