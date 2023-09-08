import configparser
import datetime
import json
import random
import sqlite3
import time

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from aiogram.types import InputMedia, InputFile
from aiogram.utils import executor

import keyboard,nowpayments
from aiogram.utils.markdown import hide_link


config = configparser.ConfigParser()
config.read("settings.ini")

TOKEN = config["BASIC"]["TOKEN"]
PAYMENT = config["BASIC"]["PAYMENT"]


bot = Bot(TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage)

dict_messages = {
    "welcome":"Welcome message here",

}

@dp.message_handler(commands=["start", "menu"], state='*')
async def start(message: types.Message,state:FSMContext):
    await message.answer(dict_messages["welcome"],reply_markup=await keyboard.main())




@dp.message_handler(content_types=["web_app_data"], state='*')
async def invoice(message: types.Message):
    orderData = json.loads(message.web_app_data.data)
    await message.answer(f"<b>Address</b>\nPhone: {orderData['telNumber']}\nAddress: {orderData['address']}",parse_mode='HTML')
    await bot.send_invoice(message.chat.id,
                           "Order",f"""{orderData["product_id"]}({orderData["size"]},{orderData["extra"]})""",
                           "test-invoice-payload",
                           PAYMENT,
                           'USD',
                           [types.LabeledPrice("Order",int(orderData["price"])*100)],
                           )


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT, state='*')
async def succesPay(message: types.Message):
    print(message.successful_payment.order_info)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
