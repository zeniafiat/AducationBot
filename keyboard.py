
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Физика')],
    [KeyboardButton(text='Скоро новое')]
    ], resize_keyboard=True)

fisickeyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Формула из физики')],
    [KeyboardButton(text='Все константы')], 
    [KeyboardButton(text='Назад')]
    ], resize_keyboard=True)
