import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ("8702227603:AAHQKJZY7l2YU-zyzTBP5Fjzr7aM0AlRMq8")
REF_LINK = "https://t.me/mira?start=ref_5950919176"
CHANNEL_LINK = "https://t.me/+bXkiv2TDeX00MmEy"


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Перейти по ссылке", url=REF_LINK)],
        [InlineKeyboardButton(text="📌 Я перешёл", callback_data="done")]
    ])

    await message.answer(
        "Перейди по ссылке и вернись 👇",
        reply_markup=kb
    )

@dp.callback_query(F.data == "done")
async def done(call: CallbackQuery):

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔓 Получить канал", url=CHANNEL_LINK)]
    ])

    await call.message.answer(
        "Готово. Вот доступ:",
        reply_markup=kb
    )

    await call.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())