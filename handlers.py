from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html, Router, F
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from AducationBot.sql import get_random_row_from_sqlite , get_all_const

from  AducationBot.keyboard import keyboard, fisickeyboard

table = ""
formula = ''

rot = Router()
@rot.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"""Hello, {message.from_user.full_name}!
я бот который поможет с запоминанием и зубрёжкой""", reply_markup=keyboard)


@rot.message(lambda message: message.text.lower() == "физика")
async def echo_handler(message: Message):
    try:
        global table
        table = "fisic"
        await message.answer("выбрана физика", reply_markup=fisickeyboard)
    except:
        await message.answer("ошибка", reply_markup=keyboard)

@rot.message(lambda message: message.text.lower() == "формула из физики")
async def echo_handler(message: Message):
    try:
        global table
        table = 'fisic'
        global formula
        data = get_random_row_from_sqlite(table_name=table)
        index, topic, name, formula = map(str, data)
        result = f"{topic}:   {name}" 
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
        text="получить ответ",
        callback_data="formula")
        )
        await message.answer(result, reply_markup=builder.as_markup())
    except:
        await message.answer("не удалось получить информацию!", reply_markup=keyboard)

@rot.message(lambda message: message.text.lower() == "все константы")
async def echo_handler(message: Message):
    try:
        global table
        table = "fisicCONST"
        one_result = get_all_const(table)
        result =""
        for i in one_result:
            result += f"{i} \n \n"
        await message.answer(str(result), reply_markup=fisickeyboard)
    except:
        await message.answer("не удалось получить информацию!", reply_markup=keyboard)

@rot.message(lambda message: message.text.lower() == "назад")
async def echo_handler(message: Message):
    try:
        global table
        table = ""
        print(keyboard)
        await message.answer("Готово", reply_markup=keyboard)
    except:
        await message.answer("ошибка", reply_markup=keyboard)

@rot.callback_query(F.data == "formula")
async def send_random_value(callback: types.CallbackQuery):
    global formula
    await callback.message.answer(str(formula))
