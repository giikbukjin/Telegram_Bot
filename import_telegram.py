import telegram
import asyncio
import pytz
import datetime

token = "YOUR TOKEN"
bot = telegram.Bot(token = token)
public_chat_name = '@Giikbuk'
chat_id = "-1001996914528"

async def print_message():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    text = "30분마다 메세지 전송, 23:00 ~ 06:00 출력 금지"

    if now.hour >= 23 or now.hour <= 6: # 23:00 ~ 06:00 메세지 출력 금지
        return
    await bot.sendMessage(chat_id, text)

async def run():
    while True:
        await print_message()
        await asyncio.sleep(1800) # 30분 단위로 메세지 전송

if __name__ == "__main__":
    asyncio.run(run())