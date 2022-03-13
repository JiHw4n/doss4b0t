import requests
from bs4 import BeautifulSoup
import os
import time
import telegram
import random

bot = telegram.Bot(token='1341257971:AAGGw6hzcd5l0v4nbAjq1pO3bK-MisLNyPA')
chat_id = bot.getUpdates()[-1].message.chat.id
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('http://corearoadbike.com/board/board.php?g_id=recycle02&t_id=Menu01Top6&category=%ED%8C%90%EB%A7%A4', headers=headers)
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('td.list_title_B > a')
    latest = posts[0].text

    with open(os.path.join(BASE_DIR, 'latest.txt') , 'r+', encoding='UTF8') as f_read:
        before = f_read.readline()
        if before != latest:
            contents = soup.select('td.list_content_B')
            latest2 = contents[0].text
            # bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요')
            bot.sendMessage(chat_id=chat_id, text=latest+latest2)
            time.sleep(random.uniform(4, 6))
        else:
            # bot.sendMessage(chat_id=chat_id, text='새 글이 없어요')
            print("새 글이 없어요")
            time.sleep(random.uniform(4,6))
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+', encoding='UTF8') as f_write:
        f_write.write(latest)
        f_write.close()