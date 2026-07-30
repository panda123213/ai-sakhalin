import requests
import json

url='http://localhost:11434/api/generate'

system_role=system_role = "Ты — помощник, который читает файл и отвечает на вопросы только по его содержанию. Если в файле нет ответа на вопрос — скажи: 'В файле нет информации об этом'. Если вопрос просит пересказать файл или спросить, о чём он — ты пересказываешь содержимое файла."

print('добро пожаловать в чат с ИИ читающий файлы. напишите выход для завершения.\n')

while True:
    user_input=input('Ты:')
    if user_input.lower()=='выход':
        break

    with open("notes.txt", "r", encoding="utf-8") as f:
        file_content = f.read()


    full_prompt=f"{system_role}\n\nСодержимое файла:\n{file_content}\n\nВопрос пользователя: {user_input}"

    data={
        'model':'llama3.2:3b',
        'prompt':full_prompt,
        'stream':False

    }
    response=requests.post(url,json=data)
    result=response.json()
    assistant_reply= result['response']

    print(f'ии:{assistant_reply}\n')