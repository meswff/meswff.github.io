from flask import Flask, render_template, request, jsonify

import subprocess
import datetime
import time
import asyncio

from getinfo import get_info_about_sale

from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

app = Flask(__name__)


def php_argv(script_path, argument, argument2, argument3, argument4):
    p = subprocess.Popen(['php', script_path, argument, argument2, argument3, argument4], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result

@app.route('/<id_crm>/<id_user>/<id_offer>')
def index(id_crm, id_user, id_offer):
  if id_offer != 'highLightTitle.png':
    result = get_info_about_sale(int(id_offer))
    print(result)
    employee_id = result['employee_id']
    print(employee_id)
    customer_id = result['customer_id']
    sale_stage_id = result['sale_stage_id']
    name_full = result['name']
    phone = result['phone']
    email = result['email']

    
    statuses = {
      '66': 'NEW',
      '67': 'Звонок совершен',
      '64': 'Собеседование назначено',
      '29': 'Собеседование проведено',
      '30': 'Обучение началось',
      '68': 'Остался через 14 дней',
      '69': 'Остался через 30 дней',
      '31': 'Приняли на работу',
      '32': 'Закрыли сделку',
      
      '55': 'Новый',
      '54': 'Неотвеченный',
      '56': 'Уточненный',
      '57': 'Отложенный спрос',
      '58': 'Приглашение',
      '59': 'Встреча',
      '65': 'Без договора',
      '60': 'Договор',
      '61': 'Задаток',
      '62': 'Закрытие сделки',
      '63': 'Отказ',
      '73': 'АВТООБЗВОН',
      '72': 'Дубль/брак'
    }
    
    try:
      if  int(employee_id) == int(id_user):
        if statuses[sale_stage_id] == 'NEW' or statuses[sale_stage_id] == 'Звонок совершен' or statuses[sale_stage_id] == 'Собеседование назначено' or statuses[sale_stage_id] == 'Собеседование проведено' or statuses[sale_stage_id] == 'Обучение началось' or statuses[sale_stage_id] == 'Остался через 14 дней' or statuses[sale_stage_id] == 'Остался через 30 дней' or statuses[sale_stage_id] == 'Приняли на работу' or statuses[sale_stage_id] == 'Закрыли сделку':
          return render_template('index_job.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id], lead_status=statuses[sale_stage_id], sale_id=id_offer)
        else:
          return render_template('index_client.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id], lead_status=statuses[sale_stage_id], sale_id=id_offer, data_value='2017-06-01T08:30')
      else:
        return render_template('403.html'), 403
    except:
      return render_template('403.html'), 403

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    
    saleid = data['saleid']
    try:
        year_and_moth = data['date'].split('-')
        day = str(year_and_moth[2])[0:-6]
        datatime = str(year_and_moth[2]).split('T')
        result_time = str(datatime[1]).split(':')
        date_time = datetime.datetime(int(year_and_moth[0]), int(year_and_moth[1]), int(day), int(result_time[0]), int(result_time[1]))
        unix_time = int(time.mktime(date_time.timetuple()))
    except:
        unix_time = None
    try: 
        comment = data['comment']
    except:
        comment = None
    
    array = list([saleid, data['status'], unix_time, comment])
    php_argv('update.php', str(saleid), str(data['status']), str(unix_time), str(data['comment']))
    
    return jsonify({'result': data})


async def send_message_newdeal_async(telegram_id, employee_id, id_offer, stage_deal):
  bot = Bot("6509666991:AAGYPMfmzqeo-wonBzjY4gB0CVgUOLsVW3w")
  statuses = {
      '66': 'NEW',
      '67': 'Звонок совершен',
      '64': 'Собеседование назначено',
      '29': 'Собеседование проведено',
      '30': 'Обучение началось',
      '68': 'Остался через 14 дней',
      '69': 'Остался через 30 дней',
      '31': 'Приняли на работу',
      '32': 'Закрыли сделку',
      
      '55': 'Новый',
      '54': 'Неотвеченный',
      '56': 'Уточненный',
      '57': 'Отложенный спрос',
      '58': 'Приглашение',
      '59': 'Встреча',
      '65': 'Без договора',
      '60': 'Договор',
      '61': 'Задаток',
      '62': 'Закрытие сделки',
      '63': 'Отказ',
      '73': 'АВТООБЗВОН',
      '72': 'Дубль/брак'
    }
  def button():
    buttons: list = [
        [
            InlineKeyboardButton(text='Перейти в CRM', web_app=WebAppInfo(url=f'https://meswff-meswff-github-io-1519.twc1.net/{telegram_id}/{employee_id}/{id_offer}'))
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
  if stage_deal != 'highLightTitle.png':
    if stage_deal == '66':
      try:
          textf = f'Новая сделка - Подбор персонала\n\nID сделки: {id_offer}\nСтадия сделки: #{statuses[stage_deal]}'
          await bot.send_message(chat_id=telegram_id, text=textf, reply_markup=button())
      except:
          pass
    elif stage_deal == '55':
      try:
        textf = f'Новая сделка - Обращение покупателя\n\nID сделки: {id_offer}\nСтадия сделки: #{statuses[stage_deal]}'
        await bot.send_message(chat_id=telegram_id, text=textf, reply_markup=button())
      except:
        pass
    else: 
      await bot.send_message(telegram_id, text=f'Вас назначили ответственным в сделке ID {id_offer}\nСтадия: #{statuses[stage_deal]}', reply_markup=button())


@app.route('/post/<telegram_id>/<employee_id>/<id_offer>/<stage_deal>')
def send_message_sync(telegram_id, employee_id, id_offer, stage_deal):
    asyncio.run(send_message_newdeal_async(telegram_id, employee_id, id_offer, stage_deal))
    return "Message sent successfully"

if __name__ == '__main__':
  app.run(ssl_context='adhoc')
