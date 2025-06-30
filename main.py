import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Аномальные сообщения
ANOMALIES = [
    "🚫 SYSTEM ERROR: ты не должен был это видеть.",
    "📁 Чат: [неизвестный контакт]\n✉️ «помоги мне выбраться»",
    "🔁 Цикл обнаружен. Отменяю отмену отмены.",
    "🕳️ Провал между строк. Содержимое утеряно.",
    "⚠️ Кто-то вошёл в чат незамеченным.",
    "✴️ Восстановление утраченных данных...",
    "👁 Ты — не ты.",
    "📴 @AnomalyBot отключён...\n...\n🟢 восстановление связи",
    "⛓ sy///ch/ro[n] err0r⛓",
    "🧠 Кто-то редактировал твою память. Не ты?",
    "📜 Это сообщение было отправлено в 2007 году. От тебя.",
]

FAKE_CONVERSATIONS = [
    "👤 [неизвестный]\n— ты здесь?\n— они следят за нами",
    "👤 [архивирован]\n— не отвечай. чат может быть подделкой.",
    "👤 [другой ты]\n— я из цикла #3. ты сбежал. я — нет.",
]

GLITCH_TEXTS = [
    "🔂 повтор. повтор. повтор. повтор. по...",
    "❓∑∆πΩΞ♜‽#₽₽₽₽₽₽",
    "📡 Нестабильность достигнута: 99%",
]

# Фантомные кнопки
phantom_keyboard = InlineKeyboardMarkup(row_width=2)
phantom_keyboard.add(
    InlineKeyboardButton("🔘 Переход разрешён", callback_data="phantom"),
    InlineKeyboardButton("🔒 Заблокировать чат", callback_data="phantom"),
)

async def send_disappearing_message(chat_id, text, delay=7):
    msg = await bot.send_message(chat_id, text)
    await asyncio.sleep(delay)
    try:
        await bot.delete_message(chat_id, msg.message_id)
    except:
        pass

async def send_random_anomaly(chat_id):
    while True:
        choice = random.choice(["anomaly", "fake", "glitch", "phantom", "ghost"])
        if choice == "anomaly":
            await send_disappearing_message(chat_id, random.choice(ANOMALIES))
        elif choice == "fake":
            await send_disappearing_message(chat_id, random.choice(FAKE_CONVERSATIONS))
        elif choice == "glitch":
            await send_disappearing_message(chat_id, random.choice(GLITCH_TEXTS))
        elif choice == "phantom":
            await bot.send_message(chat_id, "Выберите действие:", reply_markup=phantom_keyboard)
        elif choice == "ghost":
            await send_disappearing_message(chat_id, "👁️ ещё один участник читает этот чат...")
        await asyncio.sleep(random.randint(15, 30))

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("🔻 Аномалия активирована. Сбои начнутся через 10 сек...")
    await asyncio.sleep(10)
    asyncio.create_task(send_random_anomaly(message.chat.id))

@dp.message_handler(commands=["glitch"])
async def glitch_handler(message: types.Message):
    for _ in range(5):
        await send_disappearing_message(message.chat.id, random.choice(ANOMALIES), delay=4)
        await asyncio.sleep(1)

@dp.message_handler(commands=["unlock_anarchy"])
async def anarchy_handler(message: types.Message):
    await message.reply("⚠️ Режим ХАОС активирован. Восприятие нестабильно.")
    for _ in range(10):
        await send_disappearing_message(message.chat.id, random.choice(ANOMALIES + FAKE_CONVERSATIONS + GLITCH_TEXTS), delay=3)
        await asyncio.sleep(2)

@dp.callback_query_handler(lambda c: c.data == "phantom")
async def phantom_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="нажатие зафиксировано. 03:47")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
