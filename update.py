import requests

def change_stage(sale_id, stage):
    url = 'http://aires.astoria-tula.ru:81/sharedapi/sales/update'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'apikey': '21d1c8300ca07c06bf8f3aac3c16c275',
        'params[id]': sale_id,
        'params[sales_status_id]': stage
    }
    
    requests.post(url, headers=headers, data=data)
    return True

def add_comment(sale_id, comment, employee_id):
    url = 'http://aires.astoria-tula.ru:81/sharedapi/sales/addComment'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'apikey': '21d1c8300ca07c06bf8f3aac3c16c275',
        'params[entity_id]': sale_id,
        'params[text]': comment,
        'params[author]': employee_id
    }

    requests.post(url, headers=headers, data=data)
    return True
