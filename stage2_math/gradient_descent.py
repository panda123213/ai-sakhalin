import matplotlib.pyplot as plt

def f(x):
    return x**2+2*x+1

def df(x):
    return 2*x+2

def gradient_descent(start_x,learning_rate,steps):
    x=start_x
    history=[x]
    for _ in range (steps):
        grad=df(x)
        x=x-learning_rate*grad
        history.append(x)
    return x, history

start=5.0
rate=0.1
steps=20
min_x,path=gradient_descent(start,rate,steps)

print(f'минимум найден в x = {min_x:.4f}')
print(f'значение функции в минимуме:{f(min_x):.4f}')
print(f'путь спуска:{[round(p,2) for p in path]}')

x_vals = [i * 0.1 for i in range(-30, 20)]
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x) = x² + 2x + 1")
plt.scatter(path, [f(p) for p in path], color='red', label="Шаги спуска")
plt.plot(path, [f(p) for p in path], color='red', linestyle='--', alpha=0.5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Градиентный спуск к минимуму")
plt.legend()
plt.grid(True)
plt.show()