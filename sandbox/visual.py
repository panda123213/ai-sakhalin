import matplotlib.pyplot as plt
import re

def build_histogram_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Находим все числа в тексте (целые и дробные)
    numbers = [float(x) for x in re.findall(r'\d+\.?\d*', text)]
    
    if not numbers:
        return "В файле нет чисел"
    
    # Строим гистограмму
    plt.hist(numbers, bins=20, edgecolor='black', alpha=0.7)
    plt.title("Гистограмма чисел из файла")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig("histogram_from_file.png")
    plt.close()
    
    return f"Гистограмма сохранена. Найдено чисел: {len(numbers)}"