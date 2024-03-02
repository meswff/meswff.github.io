from flask import Flask, render_template, request, jsonify

import subprocess
import json
import datetime
import time
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

app = Flask(__name__)

bot = Bot("6509666991:AAGYPMfmzqeo-wonBzjY4gB0CVgUOLsVW3w")
dp = Dispatcher()

def php(script_path, argument):
  p = subprocess.Popen(['php', script_path, argument], stdout=subprocess.PIPE)
  result = p.communicate()[0]
  return result

def php_argv(script_path, argument, argument2, argument3, argument4):
    p = subprocess.Popen(['php', script_path, argument, argument2, argument3, argument4], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result

@app.route('/<id_crm>/<id_user>/<id_offer>')
def index(id_crm, id_user, id_offer):
  result = php('byid.php', id_offer)
  print(result)
  my_dict = json.loads(result)
  print(my_dict)

  try:
    employee_id = my_dict['employee_id']
  except:
    employee_id = 'Отсутствует'

  try:
    customer_id = my_dict['customers_id']
  except:
    customer_id = 'Отсутствует'
    
  sale_stage_id = my_dict['sale_stage_id']
  
  try:
    name_full = my_dict['0']['name'] + ' ' + my_dict['0']['surname']
  except:
    try:
      name_full = my_dict['0']['name']
    except:
      name_full = 'Отсутствует'

  try:
    phone = my_dict['0']['phone'][0]['phone']
  except:
    phone = 'Отсутствует'
  try:
    email = my_dict['0']['email'][0]['mail']
  except:
    email = 'Отсутствует'

  try:
    client_text = my_dict['text']
  except:
    client_text = 'Отсутствует'
  
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
        return render_template('index_job.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id], lead_status=statuses[sale_stage_id], sale_id=id_offer, user_comment=my_dict['comment'], client_text=client_text)
      else:
        return render_template('index_client.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id], lead_status=statuses[sale_stage_id], sale_id=id_offer, user_comment=my_dict['comment'], client_text=client_text, data_value='2017-06-01T08:30')
    else:
      return render_template('403.html'), 403
  except:
    return render_template('403.html'), 403

@app.route('/process_data', methods=['POST'])
def process_data():
  data = request.get_json()

  saleid = data['saleid']
  year_and_moth = data['date'].split('-')
  day = str(year_and_moth[2])[0:-6]
  datatime = str(year_and_moth[2]).split('T')
  result_time = str(datatime[1]).split(':')
  date_time = datetime.datetime(int(year_and_moth[0]), int(year_and_moth[1]), int(day), int(result_time[0]), int(result_time[1]))
  
  unix_time = int(time.mktime(date_time.timetuple()))
  array = list([saleid, data['status'], unix_time, data['comment']])
  php_argv('update.php', str(saleid), str(data['status']), str(unix_time), str(data['comment']))

  return jsonify({'result': data})


async def send_message_async(token, chat_id, message):
    bot = Bot(token)
    await bot.send_message(chat_id, message)

@app.route('/post/<token>/<chat_id>/<message>')
def send_message_sync(token, chat_id, message):
    asyncio.run(send_message_async(token, chat_id, message))

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot, handle_as_tasks=True)

@app.get(rule='/start_bot')
def start_bot():
    bot_process = Process(target=asyncio.run(main()))
    bot_process.start()
    return str(bot_process.pid)

if __name__ == '__main__':
  app.run(ssl_context='adhoc')
