import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані
t = np.array([326, 426, 526, 626, 726, 826, 926, 1026])
y = np.array([55.24, 68.66, 80.83, 91.82, 101.71, 110.56, 118.42, 125.36])

# Побудова x-вектора
x = (t - 326) / 100

# --- Лінійна апроксимація ---
p_lin = np.polyfit(x, y, 1)
y_lin = np.polyval(p_lin, x)
error_lin = np.abs(y - y_lin)
mean_error_lin = np.mean(error_lin)

# --- Квадратична апроксимація ---
p_quad = np.polyfit(x, y, 2)
y_quad = np.polyval(p_quad, x)
error_quad = np.abs(y - y_quad)
mean_error_quad = np.mean(error_quad)

# --- Показникова апроксимація ---
lny = np.log(y)
p_exp = np.polyfit(x, lny, 1)
B = p_exp[0]
A = np.exp(p_exp[1])
y_exp = A * np.exp(B * x)
error_exp = np.abs(y - y_exp)
mean_error_exp = np.mean(error_exp)

# --- Вивід результатів з підписами до завдань ---
print("=== Завдання 2а: Лінійна апроксимація ===")
print(f'Модель: y = {p_lin[0]:.4f} * x + {p_lin[1]:.4f}')
print(f'Середня абсолютна похибка: {mean_error_lin:.4f}\n')

print("=== Завдання 2б: Квадратична апроксимація ===")
print(f'Модель: y = {p_quad[0]:.4f} * x^2 + {p_quad[1]:.4f} * x + {p_quad[2]:.4f}')
print(f'Середня абсолютна похибка: {mean_error_quad:.4f}\n')

print("=== Завдання 2в: Показникова апроксимація ===")
print(f'Модель: y = {A:.4f} * exp({B:.4f} * x)')
print(f'Середня абсолютна похибка: {mean_error_exp:.4f}\n')

# --- Побудова графіка ---
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ko', label='Експериментальні дані')
plt.plot(x, y_lin, '-b', label='Лінійна апроксимація')
plt.plot(x, y_quad, '-r', label='Квадратична апроксимація')
plt.plot(x, y_exp, '-g', label='Показникова апроксимація')
plt.xlabel('x = (t - 326) / 100')
plt.ylabel('y')
plt.title('Апроксимація експериментальних даних методом найменших квадратів')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

