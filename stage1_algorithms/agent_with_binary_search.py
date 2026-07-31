import requests
import json
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_in_file(file_path,target_word):
    with open(file_path,'r',encoding='utf-8')as f:
        words=f.read().split()
        words_sorted=sorted(words)
        index=binary_search(words_sorted,target_word)
        if index !=-1:
            return f'слово {target_word} найдено в файле '
        else:
            return f"Слово '{target_word}' не найдено."

url='http://localhost:11434/api/generate'

system_role = """
Ты — помощник, который читает файл и отвечает на вопросы только по его содержанию.

Правила:
1. Если пользователь спрашивает 'о чём файл' — ты даёшь краткий пересказ файла (1–2 предложения).
2. Если вопрос не по файлу — отвечаешь: 'В файле нет информации об этом'.
3. Всегда отвечай кратко и по делу.
"""

print('добро пожаловать в чат с ИИ читающий файлы. напишите выход для завершения.\n')

while True:
    user_input=input('Ты:')
    if user_input.lower()=='выход':
        break
    if 'найди слово' in user_input.lower():
        word=user_input.split()[-1]
        response = binary_search_in_file("stage1_algorithms/notes.txt", word)
        print(f'ИИ: {response}\n')
        continue  

    with open("stage1_algorithms/notes.txt", "r", encoding="utf-8") as f:
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