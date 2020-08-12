import sys
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

TOKEN = ' ' # API Token

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    pprint(msg)

    if msg['chat']['id'] == 407xxxxxx : #sender id
        if content_type == 'text':
            bot.sendMessage(-1001207xxxxxx, msg['text']) #group id
    

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
