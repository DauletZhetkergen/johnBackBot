import sqlite3

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.callback_data import CallbackData

async def main():
    mark = InlineKeyboardMarkup()
    mark.add(InlineKeyboardButton('Category',web_app=WebAppInfo(url="https://8203-95-57-85-40.ngrok-free.app")))
    return mark
