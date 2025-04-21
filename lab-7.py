import numpy as np
import matplotlib.pyplot as plt

# === Завдання 1 ===
# Побудова моделей апроксимації: лінійна, квадратична, показникова, гіперболічна, степенева, логарифмічна

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([52.44, 65.86, 78.03, 89.02, 98.91, 107.76, 115.62, 122.56])
n = len(x)

# Уникнення ділення на нуль, замінюємо x=0 на дуже мале значення для гіперболічної та логарифмічної моделей
x_safe = np.where(x == 0, 1e-6, x)

# === Лінійна апроксимація y = a*x + b ===
A_lin = np.vstack([x, np.ones(n)]).T
params_lin = np.linalg.lstsq(A_lin, y, rcond=None)[0]
a_lin, b_lin = params_lin[0], params_lin[1]
y_lin = a_lin * x + b_lin

# === Квадратична апроксимація y = a*x^2 + b*x + c ===
A_quad = np.vstack([x**2, x, np.ones(n)]).T
params_quad = np.linalg.lstsq(A_quad, y, rcond=None)[0]
a_quad, b_quad, c_quad = params_quad
y_quad = a_quad * x**2 + b_quad * x + c_quad

# === Показникова апроксимація y = a * b^x ===
log_y = np.log(y)
A_exp = np.vstack([x, np.ones(n)]).T
params_exp = np.linalg.lstsq(A_exp, log_y, rcond=None)[0]
ln_b, ln_a = params_exp
a_exp = np.exp(ln_a)
b_exp = np.exp(ln_b)
y_exp = a_exp * b_exp**x

# === Гіперболічна апроксимація y = a/x + b ===
A_hyper = np.vstack([1/x_safe, np.ones(n)]).T
params_hyper = np.linalg.lstsq(A_hyper, y, rcond=None)[0]
a_hyper, b_hyper = params_hyper
y_hyper = a_hyper / x_safe + b_hyper

# === Степенева апроксимація y = a * x^b ===
log_x = np.log(x_safe)
log_y = np.log(y)
A_power = np.vstack([log_x, np.ones(n)]).T
params_power = np.linalg.lstsq(A_power, log_y, rcond=None)[0]
b_power, ln_a_power = params_power
a_power = np.exp(ln_a_power)
y_power = a_power * x_safe**b_power

# === Логарифмічна апроксимація y = a * ln(x) + b ===
A_log = np.vstack([np.log(x_safe), np.ones(n)]).T
params_log = np.linalg.lstsq(A_log, y, rcond=None)[0]
a_log, b_log = params_log
y_log = a_log * np.log(x_safe) + b_log

# === Похибки апроксимації ===
def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

err_lin = mae(y, y_lin)
err_quad = mae(y, y_quad)
err_exp = mae(y, y_exp)
err_hyper = mae(y, y_hyper)
err_power = mae(y, y_power)
err_log = mae(y, y_log)

print("\n=== Завдання 1 ===")
print("Визначення апроксимаційних моделей та оцінка точності")

print("\n=== Лінійна апроксимація ===")
print("Формула: y = a * x + b")
print(f"y = {a_lin:.4f} * x + {b_lin:.4f}")
print(f"Середня абсолютна похибка: {err_lin:.3f}")

print("\n=== Квадратична апроксимація ===")
print("Формула: y = a * x^2 + b * x + c")
print(f"y = {a_quad:.4f} * x^2 + {b_quad:.4f} * x + {c_quad:.4f}")
print(f"Середня абсолютна похибка: {err_quad:.3f}")

print("\n=== Показникова апроксимація ===")
print("Формула: y = a * b^x")
print(f"y = {a_exp:.4f} * {b_exp:.4f}^x")
print(f"Середня абсолютна похибка: {err_exp:.3f}")

print("\n=== Гіперболічна апроксимація ===")
print("Формула: y = a / x + b")
print(f"y = {a_hyper:.4f} / x + {b_hyper:.4f}")
print(f"Середня абсолютна похибка: {err_hyper:.3f}")

print("\n=== Степенева апроксимація ===")
print("Формула: y = a * x^b")
print(f"y = {a_power:.4f} * x^{b_power:.4f}")
print(f"Середня абсолютна похибка: {err_power:.3f}")

print("\n=== Логарифмічна апроксимація ===")
print("Формула: y = a * ln(x) + b")
print(f"y = {a_log:.4f} * ln(x) + {b_log:.4f}")
print(f"Середня абсолютна похибка: {err_log:.3f}")

# === Завдання 2 ===
plt.plot(x, y, 'ko-', label='Дані')
plt.plot(x, y_lin, 'r--', label='Лінійна')
plt.plot(x, y_quad, 'g-.', label='Квадратична')
plt.plot(x, y_exp, 'b:', label='Показникова')
plt.plot(x, y_hyper, 'c--', label='Гіперболічна')
plt.plot(x, y_power, 'm:', label='Степенева')
plt.plot(x, y_log, 'y-.', label='Логарифмічна')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
