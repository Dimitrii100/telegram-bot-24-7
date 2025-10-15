import asyncio
from telegram import Bot
import os
from fastapi import FastAPI
import uvicorn

TOKEN = os.environ.get('8488417788:AAGiM0rdwonatxAZ53KwkaRaCgES4E5LXs0')
CHAT_ID = os.environ.get('611001716')
PORT = int(os.environ.get('PORT', 10000))  # Render сам задает порт

bot = Bot(token=TOKEN)
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

async def send_message(text):
    await bot.send_message(chat_id=CHAT_ID, text=text)

async def repeat_every_10_seconds():
    while True:
        await send_message("все ое")
        await asyncio.sleep(10)  # ждем 10 секунд

async def main_bot_loop():
    # Отправляем сообщение сразу при старте
    await send_message("все ое (бот запущен)")
    # Запускаем повторяющееся отправление сообщений
    await repeat_every_10_seconds()

# Запуск бота и веб-сервиса одновременно
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Запускаем бот в фоне
    loop.create_task(main_bot_loop())
    # Запускаем FastAPI для пинга
    uvicorn.run(app, host="0.0.0.0", port=PORT)
