import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Аномальные фразы
ANOMALY_MESSAGES = [
    "🚫 SYSTEM ERROR: ты не должен был это видеть.",
    "📁 Чат: [неизвестный контакт]\n✉️ Сообщение: «помоги мне выбраться»",
    "🔁 Цикл обнаружен. Отменяю отмену отмены.",
    "📡 Получено сообщение от несуществующего собеседника.",
    "⚠️ Внимание. Кто-то вошёл в этот чат без уведомления.",
    "🕳️ Провал между строк. Содержимое утеряно.",
    "✴️ Данные из памяти пользователя восстановлены...",
]

async def send_anomaly(chat_id):
    while True:
        msg = random.choice(ANOMALY_MESSAGES)
        await bot.send_message(chat_id, msg)
        await asyncio.sleep(random.randint(15, 30))

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("🔻 Аномалия активирована. Ожидайте сбои...")
    asyncio.create_task(send_anomaly(message.chat.id))

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
