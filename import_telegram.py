import telegram
import asyncio
import schedule
import time

async def send_bot_message():
    token = "6813558981:AAGEecosIF7E25qekSFF9CrmNb36LLiTRRE"
    bot = telegram.Bot(token = token)
    public_chat_name = '@GiikbukTest'
    chat_id = "-1001996914528"
    #chat_id = "6911063520"
    #asyncio.run(bot.send_message(chat_id=chat_id, text="hello"))
    now = time.localtime()
    text = "current time = ", str(now)

    asyncio.run(bot.send_message(chat_id = public_chat_name, text = text))

while True:
    send_bot_message()
    time.sleep(1)