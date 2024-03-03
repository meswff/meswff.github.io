import requests
import json


def get_info_about_sale(sale_id):
    url = 'http://aires.astoria-tula.ru:81/sharedapi/sales/filter'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'apikey': '21d1c8300ca07c06bf8f3aac3c16c275',
        'params[byid]': sale_id
    }

    response = requests.post(url, headers=headers, data=data)
    my_dict = json.loads(response.text)
    id_customer = my_dict['data']['list'][0]

    url = 'http://aires.astoria-tula.ru:81/sharedapi/purchaser/filter'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'apikey': '21d1c8300ca07c06bf8f3aac3c16c275',
        'params[byid]': id_customer['customers_id']
    }

    response = requests.post(url, headers=headers, data=data)
    dict = json.loads(response.text)['data']['list'][0]

    try:
        name = str(dict['name']) + ' ' + str(dict['surname'])
    except:
        name = 'Отсутствует'

    try:
        email = dict['email'][0]['email']
    except:
        email = 'Отсутствует'

    try:
        if dict['text'] != None:
            text = dict['text']
    except:
        text = 'Отсутствует'

    try:
        return {
            'employee_id': id_customer['employee_id'],
            'id_offer': sale_id,
            'sale_stage_id': id_customer['sale_stage_id'],
            'customer_id': id_customer['customers_id'],
            'name': name,
            'phone': dict['phone'][0]['phone'],
            'text': text,
            'email': email
        }
    except Exception as E:
        return E
