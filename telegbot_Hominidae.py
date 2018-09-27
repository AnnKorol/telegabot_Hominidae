import requests
import datetime

url = "https://api.telegram.org/bot637395215:AAHVL1tdFrKGQP6eoGbREzw6Lf4XBmaoxu8/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id
def get_last_message_id(update):  
    message = update['message']['date']['text']#не работает, хз почему
    return message
def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': texts}
    response = requests.post(url + 'sendMessage', data=params)
    
    return response
while True:
    chat_id = get_chat_id(last_update(get_updates_json(url)))
    last_msg_id = get_last_message_id(last_update(get_updates_json(url)))
    if last_msg_id == "Hi":
        send_mess(chat_id, 'Hi!')
    print(last_msg_id)
