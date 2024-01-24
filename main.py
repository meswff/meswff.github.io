from flask import Flask, render_template

import subprocess
import json

app = Flask(__name__)

def php(script_path, argument):
  p = subprocess.Popen(['php', script_path, argument], stdout=subprocess.PIPE)
  result = p.communicate()[0]
  return result

@app.route('/<id_offer>')
def index(id_offer):
  result = php('C:\\Users\\meswff\\Desktop\\crm_intrup\\byid.php', id_offer)
  my_dict = result
  print(result)
  
  customer_id = my_dict['0']['customers_id']
  sale_stage_id = my_dict['0']['sale_stage_id']
  
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
    return render_template('index_job.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id])
  else:
    return render_template('index_client.html', user_username=name_full, user_id=customer_id, user_info=statuses[sale_stage_id], user_ip='В обработке', user_phone=phone, user_mail=email, user_status=statuses[sale_stage_id])

if __name__ == '__main__':
  app.run(ssl_context='adhoc')
