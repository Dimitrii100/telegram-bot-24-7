import asyncio
import threading
from aiohttp import web
from telegram import Bot
import os

# --- Чтение переменных окружения ---
BOT_TOKEN = os.environ.get("8488417788:AAGiM0rdwonatxAZ53KwkaRaCgES4E5LXs0")
CHAT_ID = os.environ.get("611001716")

# Проверка переменных
if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("❌ BOT_TOKEN или CHAT_ID не заданы в окружении!")

bot = Bot(token=BOT_TOKEN)

# --- Телеграм-цикл ---
async def send_periodic_message():
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text="✅ Всё работает (Render живой)")
            print("Сообщение отправлено")
        except Exception as e:
            print(f"Ошибка отправки: {e}")
        await asyncio.sleep(10)

# --- HTTP-сервер для Render + UptimeRobot ---
async def handle(request):
    return web.Response(text="✅ I'm alive!")

def run_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    port = int(os.environ.get("PORT", 10000))  # Render выдаёт порт через PORT
    web.run_app(app, host="0.0.0.0", port=port)

# --- Основной запуск ---
if __name__ == "__main__":
    # Запускаем HTTP-сервер в отдельном потоке
    threading.Thread(target=run_web_server, daemon=True).start()
    # Запускаем цикл отправки сообщений
    asyncio.run(send_periodic_message())
