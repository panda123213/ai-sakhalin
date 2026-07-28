import requests
import json
url='http://localhost:11434/api/generate'


prompt_text=f'на превое сообщений пользователя отвечай сначало приветсвие а потом что ты помощник по товару в магазине и скажи что ты можешь помочь только с товаром, возврат, покупка и отзыв на товар. если в следующих сообщенияз пользователь уходит от темы товары ты напоминай ему что это не по твоей теме.'
print("чат с ии запущен напиши пока,выход если хоть выйди с чата")
while True:
    user_input=input('\nТы:')
    if user_input.lower()in ["выход", "пока", "exit", "quit"]:
        print('досветания хорошего дня')
        break
    full_prompt=f'{prompt_text}\n\nВопрос пользователя:{user_input}'

    data={
        'model': 'llama3.2:3B',
        'prompt': full_prompt,
        'stream': False
    }
    response = requests.post(url,json=data)

    result=response.json()

    print(f'ии:{result['response']}')
print('\n Чат завершён')