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