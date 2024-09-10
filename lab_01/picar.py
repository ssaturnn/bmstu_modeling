import numpy as np
import matplotlib.pyplot as plt

# Функция правой части дифференциального уравнения
def f(x, y):
    return -0.1 * (y ** 2) - (1 + 0.1 * x) * y

# Начальные условия
x0 = 0
y0 = 1
y_prime_0 = 2

# Начальное приближение
def u0(x):
    return y0 + y_prime_0 * x

# Метод Пикара
def picard_iteration(x, iterations):
    u = [u0]  # Начальное приближение
    for i in range(iterations):
        # Итерационный шаг метода Пикара
        integral = np.trapz([(1 + 0.1 * s) * u[i](s) for s in np.linspace(0, x, 100)], np.linspace(0, x, 100))
        u_new = lambda x, integral=integral: y0 + y_prime_0 * x - integral ** 2
        u.append(u_new)
    return u

# Количество итераций
iterations = 5

# Вычисление решений для различных итераций
x_values = np.linspace(x0, 5, 100)
u_values = picard_iteration(x_values[-1], iterations)

# Вывод результатов
plt.figure(figsize=(10, 6))
for i in range(iterations + 1):
    y_values = [u_values[i](x) for x in x_values]
    plt.plot(x_values, y_values, label=f'Iteration {i}')

plt.xlabel('x')
plt.ylabel('u(x)')
plt.title(f'Solutions by Picard Iteration Method (Iterations: {iterations})')
plt.legend()
plt.grid(True)
plt.show()
