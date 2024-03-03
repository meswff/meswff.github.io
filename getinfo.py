import requests
import json


def get_info_about_sale():
    url = 'http://aires.astoria-tula.ru:81/sharedapi/sales/getbychangestage'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'apikey': '21d1c8300ca07c06bf8f3aac3c16c275',
        'params[date_start]': '2024-02-15',
        'params[date_end]': '2030-01-01'
    }

    response = requests.post(url, headers=headers, data=data)

    my_dict = json.loads(response.text)
    sale_id = my_dict['data']['list'][-1]['sale_id']

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

    try:
        return {
            'current_id': sale_id,
            'employee_id': id_customer['employee_id'],
            'id_offer': sale_id,
            'sale_stage_id': id_customer['sale_stage_id']
        }
    except:
        return 'Ошибка при попытке получить данные'



def get_info_about_worker(employee_id):

    url = 'http://aires.astoria-tula.ru:81/sharedapi/worker/filter'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'apikey': '21d1c8300ca07c06bf8f3aac3c16c275',
        'params[id]': employee_id
    }

    response = requests.post(url, headers=headers, data=data)
    my_dict = json.loads(response.text)
    try:
        return my_dict['data'][str(employee_id)]['fields']['3643']['value']
    except:
        return 'Информафия о работнике не найдена'

