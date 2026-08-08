import random

rolls=1000
counts={i: 0 for i in range(1,7)}
for _ in range(rolls):
    result=random.randint(1,6)
    counts[result]+=1
print("Частота выпадения каждой грани:")
for face, count in counts.items():
    print(f"{face}: {count} раз")

# 2. Вероятность = частота / общее количество бросков
print("\nВероятность (эмпирическая):")
for face, count in counts.items():
    prob = count / rolls
    print(f"P({face}) = {prob:.3f}")

# 3. Теоретическая вероятность (для идеального кубика)
print("\nТеоретическая вероятность (для идеального кубика):")
theoretical = 1/6
print(f"P(каждая грань) = {theoretical:.3f}")