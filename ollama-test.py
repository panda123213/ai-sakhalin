# созадание первого ии чата (ollama)

# import requests
# import json
# url='http://localhost:11434/api/generate'


# prompt_text=f'на превое сообщений пользователя отвечай сначало приветсвие а потом что ты помощник по товару в магазине и скажи что ты можешь помочь только с товаром, возврат, покупка и отзыв на товар. если в следующих сообщенияз пользователь уходит от темы товары ты напоминай ему что это не по твоей теме.'
# print("чат с ии запущен напиши пока,выход если хоть выйди с чата")
# while True:
#     user_input=input('\nТы:')
#     if user_input.lower()in ["выход", "пока", "exit", "quit"]:
#         print('досветания хорошего дня')
#         break
#     full_prompt=f'{prompt_text}\n\nВопрос пользователя:{user_input}'

#     data={
#         'model': 'llama3.2:3B',
#         'prompt': full_prompt,
#         'stream': False
#     }
#     response = requests.post(url,json=data)

#     result=response.json()

#     print(f'ии:{result['response']}')
# print('\n Чат завершён')


# добавили память

import requests
import json

url="http://localhost:11434/api/generate"

system_role='Ты — ИИ-ассистент. Отвечай максимально кратко. Если вопрос требует одного слова — отвечай одним словом.'



print('чат с ИИ. напиши выход для завершения. \n')

while True:
    user_input=input('ты:')
    if user_input.lower()=='выход':
        break


    with open('dialog.txt','a',encoding='utf-8') as f:
        f.write(f'пользователь:{user_input}\n')

    



    with open('dialog.txt','r',encoding='utf-8') as f:
        file_history=f.read()


    full_prompt=f'{system_role}\n\nИстория диалога:\n{file_history}\n\nАссистент:'

    data={
        'model':'llama3.2:3B',
        'prompt':full_prompt,
        'stream':False,
        'options': {
            'temperature':0.3
        } 
    }
    response=requests.post(url,json=data)
    result=response.json()
    assistant_reply= result['response']
    with open("dialog.txt", "a", encoding="utf-8") as f:
        f.write(f"ИИ: {assistant_reply}\n\n")

    print(f'ии:{assistant_reply}\n')
