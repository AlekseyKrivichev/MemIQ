import asyncio
import logging
import random

from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.filters import Command
from datetime import datetime, timedelta
import config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token) # обращаемся к токену бота из config файла
dp = Dispatcher()

last_start_time = {}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    current_time = datetime.now()
    if user_id in last_start_time:
        time_diff = current_time - last_start_time[user_id]
        if time_diff < timedelta(seconds=1):
            print(f"Игнорируем дубль /start от пользователя {user_id}")
            return  # Игнорируем дубликат

    last_start_time[user_id] = current_time


    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text = config.btn1_name, callback_data = "btn1")
    button2 = types.InlineKeyboardButton(text = config.btn2_name, callback_data = "btn2")
    button3 = types.InlineKeyboardButton(text = config.btn3_name, callback_data = "btn3")
    builder.row(button1)
    builder.row(button2)
    builder.row(button3)
    await bot.send_photo(message.chat.id, photo=config.photo ,caption = config.menu_text, reply_markup = builder.as_markup())

# создание кнопок под каждым ответом 
def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text=config.btn1_name, callback_data="btn1")
    button2 = types.InlineKeyboardButton(text=config.btn2_name, callback_data="btn2")
    button3 = types.InlineKeyboardButton(text=config.btn3_name, callback_data="btn3")
    builder.row(button1)
    builder.row(button2)
    builder.row(button3)
    return builder.as_markup()



@dp.callback_query(F.data == "btn1")
async def send_random_image(callback: types.CallbackQuery):
    try:
        image_path = config.get_random_image()
        photo = FSInputFile(image_path)
        await callback.message.answer_photo(photo, reply_markup=get_inline_keyboard())
        await callback.answer()
    except IndexError:
        await callback.message.answer("В папке нет картинок 😔")
        await callback.answer()
    except Exception as e:
        await callback.message.answer("Ошибка при загрузке картинки 😔")
        await callback.answer()
        print(f"Ошибка: {e}")


@dp.callback_query(F.data == "btn2")
async def send_random_fact_btn2(callback: types.CallbackQuery):
    btn2_response = random.choice(config.file_text2).strip()
    await callback.message.answer(btn2_response, parse_mode = 'HTML', reply_markup=get_inline_keyboard())
    await callback.answer()
    await callback.answer()

@dp.callback_query(F.data == "btn3")
async def send_random_fact_btn3(callback: types.CallbackQuery):
    btn3_response = random.choice(config.file_text3).strip()
    await callback.message.answer(btn3_response, parse_mode = 'HTML', reply_markup=get_inline_keyboard())
    await callback.answer()

async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())