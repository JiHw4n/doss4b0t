import requests
from bs4 import BeautifulSoup
import os
import time

import telegram

bot = telegram.Bot(token='1341257971:AAGGw6hzcd5l0v4nbAjq1pO3bK-MisLNyPA')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('http://corearoadbike.com/board/board.php?g_id=recycle02&t_id=Menu01Top6&category=%ED%8C%90%EB%A7%A4')
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
        else:
            # bot.sendMessage(chat_id=chat_id, text='새 글이 없어요')
            time.sleep(3)
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+', encoding='UTF8') as f_write:
        f_write.write(latest)
        f_write.close()

    time.sleep(1) # 60초(1분)을 쉬어줍니다.