from flask import Flask, render_template, request, jsonify

import subprocess
import json
import datetime
import time

app = Flask(__name__)

def php(script_path, argument):
  p = subprocess.Popen(['php', script_path, argument], stdout=subprocess.PIPE)
  result = p.communicate()[0]
  return result

@app.route('/<id_offer>')
def index(id_offer):
  result = php('byid.php', id_offer)
  print(result)
  my_dict = json.loads(result)

  customer_id = my_dict['customers_id']
  sale_stage_id = my_dict['sale_stage_id']
  
  name_full = my_dict['name'] + ' ' + my_dict['surname']
  try:
    phone = my_dict['phone'][0]['phone']
  except:
    phone = 'Отсутствует'
  try:
    email = my_dict['email'][0]['mail']
  except:
    email = 'Отсутствует'
  
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
  if statuses[sale_stage_id] == 'NEW' or statuses[sale_stage_id] == 'Звонок совершен' or statuses[sale_stage_id] == 'Собеседование назначено' or statuses[sale_stage_id] == 'Собеседование проведено' or statuses[sale_stage_id] == 'Обучение началось' or statuses[sale_stage_id] == 'Остался через 14 дней' or statuses[sale_stage_id] == 'Остался через 30 дней' or statuses[sale_stage_id] == 'Приняли на работу' or statuses[sale_stage_id] == 'Закрыли сделку':
    return render_template('index_job.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id], lead_status=statuses[sale_stage_id])
  else:
    return render_template('index_client.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id], lead_status=statuses[sale_stage_id])

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
    php_argv('update.php', [saleid, data['status'], unix_time, data['comment']])
    
    
    return jsonify({'result': data})

if __name__ == '__main__':
  app.run(ssl_context='adhoc')
