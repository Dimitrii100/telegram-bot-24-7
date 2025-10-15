import asyncio
from telegram import Bot
from telegram.ext import Application

# Настройки
BOT_TOKEN = "8488417788:AAGiM0rdwonatxAZ53KwkaRaCgES4E5LXs0"
CHAT_ID = "611001716"

async def send_periodic_message():
    """Функция для отправки периодических сообщений"""
    bot = Bot(token=BOT_TOKEN)
    
    while True:
        try:
            await bot.send_message(
                chat_id=CHAT_ID,
                text="✅ Всё работает нормально!"
            )
            print(f"Сообщение отправлено в {asyncio.get_event_loop().time()}")
        except Exception as e:
            print(f"Ошибка отправки: {e}")
        
        # Ждем 10 секунд
        await asyncio.sleep(10)

async def main():
    """Основная функция"""
    print("Бот запущен...")
    await send_periodic_message()

if __name__ == "__main__":
    asyncio.run(main())