import subprocess
import asyncio
import logging
import setuptools
import json

from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

def php(script_path):
    p = subprocess.Popen(['php', script_path], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6509666991:AAGYPMfmzqeo-wonBzjY4gB0CVgUOLsVW3w')
dp = Dispatcher()

@dp.message(Command('start'))
async def apanel(message: types.Message):
    result = php('C:\\Users\\meswff\\Desktop\\crm_intrup\\main.php')
    my_dict = json.loads(result)

    id_offer = my_dict['0']['id']
    customer_id = my_dict['0']['customers_id']
    sale_stage_id = my_dict['0']['sale_stage_id']
    
    name_full = my_dict['name'] + my_dict['surname']
    phone = my_dict['phone'][0]['phone']
    email = my_dict['email']
        
    def button():
        buttons: list = [
            [
                InlineKeyboardButton(text='Перейти в CRM', web_app=WebAppInfo(url=f'https://127.0.0.1:5000/{id_offer}'))
            ]
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard
    
    textf = f'Новая сделка!\n\nID сделки: {id_offer}\nСтадия сделки: {sale_stage_id}'
    #textf = f'test\n{id_offer}\n{customer_id}\n{sale_stage_id}\n{name_full}\n{phone}\n{email}'
    
    await bot.send_message(chat_id=message.chat.id, text=textf, reply_markup=button())

async def check_id():
    last_id = '26486'
    while True:
        result = php('C:\\Users\\meswff\\Desktop\\crm_intrup\\main.php')
        my_dict = json.loads(result)
        current_id = my_dict['id']
        
        if current_id != last_id:
            await bot.send_message(chat_id="1648094852", text=f"ID has changed to {current_id}")
            last_id = current_id
        
        await asyncio.sleep(10)  # Check every 60 seconds

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot, handle_as_tasks=True)


if __name__ == "__main__":
    asyncio.run(main())
    setuptools.setup()
