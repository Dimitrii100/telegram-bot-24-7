import asyncio
import threading
from aiohttp import web
from telegram import Bot

# --- Прямо прописанные токен и ID ---
BOT_TOKEN = "8488417788:AAGiM0rdwonatxAZ53KwkaRaCgES4E5LXs0"
CHAT_ID = "611001716"

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
    port = 10000  # Render порт по умолчанию, можно заменить на 0.0.0.0:PORT
    web.run_app(app, host="0.0.0.0", port=port)

# --- Основной запуск ---
if __name__ == "__main__":
    threading.Thread(target=run_web_server, daemon=True).start()
    asyncio.run(send_periodic_message())
