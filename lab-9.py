import numpy as np

# === Завдання 1 ===
m_beta1 = 5  # сек
m_beta2 = 2  # сек
m_beta3 = np.sqrt(m_beta1**2 + m_beta2**2)
print("=== Завдання 1 ===")
print("Обчислити СКП кута β₃, якщо відомі СКП двох інших кутів трикутника:")
print(f"СКП кута β₃ = {m_beta3:.3f} сек\n")

# === Завдання 2 ===
S = 560.22  # м
alpha_deg = 20
alpha_min = 45.1
alpha = alpha_deg + alpha_min / 60  # у градусах
alpha_rad = np.radians(alpha)  # у радіанах
ms = 0.30  # м
m_alpha_min = 2.0
m_alpha_deg = m_alpha_min / 60  # у градусах
m_alpha_rad = np.radians(m_alpha_deg)  # у радіанах

delta_x = S * np.cos(alpha_rad)
delta_y = S * np.sin(alpha_rad)

m_delta_x = np.sqrt((ms * np.cos(alpha_rad))**2 + (S * np.sin(alpha_rad) * m_alpha_rad)**2)
m_delta_y = np.sqrt((ms * np.sin(alpha_rad))**2 + (S * np.cos(alpha_rad) * m_alpha_rad)**2)

print("=== Завдання 2 ===")
print("Обчислити прирости координат Δx, Δy та їхні СКП")
print(f"Δx = {delta_x:.2f} м, похибка m_Δx = {m_delta_x:.2f} м")
print(f"Δy = {delta_y:.2f} м, похибка m_Δy = {m_delta_y:.2f} м\n")

# === Завдання 3 ===
S3 = 45.28  # м
v_deg = 0
v_min = 55.4
v = v_deg + v_min / 60  # у градусах
v_rad = np.radians(v)  # у радіанах
ms3 = 0.34  # м
mv_min = 0.2
mv_deg = mv_min / 60
mv_rad = np.radians(mv_deg)

h = S3 * np.sin(v_rad)
mh = np.sqrt((ms3 * np.sin(v_rad))**2 + (S3 * np.cos(v_rad) * mv_rad)**2)

print("=== Завдання 3 ===")
print("Обчислити перевищення h та його СКП")
print(f"Перевищення h = {h:.3f} м, похибка m_h = {mh:.4f} м\n")

# === Завдання 4 ===
# y = 3x^2 - h + (3/4)z^3
x = 2.0
h = 1.5
z = 1.0
m_x = 0.05
m_h = 0.02
m_z = 0.03

y = 3 * x**2 - h + (3/4) * z**3
m_y = np.sqrt((6 * x * m_x)**2 + m_h**2 + ((9/4) * z**2 * m_z)**2)

print("=== Завдання 4 ===")
print("Обчислити значення y = 3x² - h + 3/4·z³ та його СКП")
print(f"y = {y:.3f}, похибка m_y = {m_y:.3f}\n")

# === Завдання 5 ===
# f = 3·ln(x)·tg(y)
x5 = 1.7
y5 = 0.9
m_x5 = 0.04
m_y5 = 0.03

f = 3 * np.log(x5) * np.tan(y5)
m_f = np.sqrt(((3 * np.tan(y5) / x5) * m_x5)**2 + ((3 * np.log(x5) / (np.cos(y5)**2)) * m_y5)**2)

print("=== Завдання 5 ===")
print("Обчислити значення f = 3·ln(x)·tg(y) та його СКП")
print(f"f = {f:.3f}, похибка m_f = {m_f:.3f}")

import numpy as np

# === Завдання 1 ===
m_beta1 = 5  # сек
m_beta2 = 2  # сек
m_beta3 = np.sqrt(m_beta1**2 + m_beta2**2)
print("=== Завдання 1 ===")
print("Обчислити СКП кута β₃, якщо відомі СКП двох інших кутів трикутника:")
print(f"СКП кута β₃ = {m_beta3:.3f} сек\n")

# === Завдання 2 ===
S = 560.22  # м
alpha_deg = 20
alpha_min = 45.1
alpha = alpha_deg + alpha_min / 60  # у градусах
alpha_rad = np.radians(alpha)  # у радіанах
ms = 0.30  # м
m_alpha_min = 2.0
m_alpha_deg = m_alpha_min / 60  # у градусах
m_alpha_rad = np.radians(m_alpha_deg)  # у радіанах

delta_x = S * np.cos(alpha_rad)
delta_y = S * np.sin(alpha_rad)

m_delta_x = np.sqrt((ms * np.cos(alpha_rad))**2 + (S * np.sin(alpha_rad) * m_alpha_rad)**2)
m_delta_y = np.sqrt((ms * np.sin(alpha_rad))**2 + (S * np.cos(alpha_rad) * m_alpha_rad)**2)

print("=== Завдання 2 ===")
print("Обчислити прирости координат Δx, Δy та їхні СКП")
print(f"Δx = {delta_x:.2f} м, похибка m_Δx = {m_delta_x:.2f} м")
print(f"Δy = {delta_y:.2f} м, похибка m_Δy = {m_delta_y:.2f} м\n")

# === Завдання 3 ===
S3 = 45.28  # м
v_deg = 0
v_min = 55.4
v = v_deg + v_min / 60  # у градусах
v_rad = np.radians(v)  # у радіанах
ms3 = 0.34  # м
mv_min = 0.2
mv_deg = mv_min / 60
mv_rad = np.radians(mv_deg)

h = S3 * np.sin(v_rad)
mh = np.sqrt((ms3 * np.sin(v_rad))**2 + (S3 * np.cos(v_rad) * mv_rad)**2)

print("=== Завдання 3 ===")
print("Обчислити перевищення h та його СКП")
print(f"Перевищення h = {h:.3f} м, похибка m_h = {mh:.4f} м\n")

# === Завдання 4 ===
# y = 3x^2 - h + (3/4)z^3
x = 2.0
h4 = 1.5
z = 1.0
m_x = 0.05
m_h4 = 0.02
m_z = 0.03

y = 3 * x**2 - h4 + (3/4) * z**3
m_y = np.sqrt((6 * x * m_x)**2 + m_h4**2 + ((9/4) * z**2 * m_z)**2)

print("=== Завдання 4 ===")
print("Обчислити значення y = 3x² - h + 3/4·z³ та його СКП")
print(f"y = {y:.3f}, похибка m_y = {m_y:.3f}\n")

# === Завдання 5 ===
# f = 3·ln(x)·tg(y)
x5 = 1.7
y5 = 0.9
m_x5 = 0.04
m_y5 = 0.03

f = 3 * np.log(x5) * np.tan(y5)
m_f = np.sqrt(((3 * np.tan(y5) / x5) * m_x5)**2 + ((3 * np.log(x5) / (np.cos(y5)**2)) * m_y5)**2)

print("=== Завдання 5 ===")
print("Обчислити значення f = 3·ln(x)·tg(y) та його СКП")
print(f"f = {f:.3f}, похибка m_f = {m_f:.3f}\n")

print("Результати розрахунків:")
print("{:<30} {:>10} {:>15}".format("Величина", "Значення", "СКП"))
print("-"*55)
print("{:<30} {:>10} {:>15}".format("Кут β₃ (сек)", f"{m_beta3:.3f}", "-"))
print("{:<30} {:>10} {:>15}".format("Δx (м)", f"{delta_x:.2f}", f"{m_delta_x:.2f}"))
print("{:<30} {:>10} {:>15}".format("Δy (м)", f"{delta_y:.2f}", f"{m_delta_y:.2f}"))
print("{:<30} {:>10} {:>15}".format("Перевищення h (м)", f"{h:.3f}", f"{mh:.4f}"))
print("{:<30} {:>10} {:>15}".format("Функція y", f"{y:.3f}", f"{m_y:.3f}"))
print("{:<30} {:>10} {:>15}".format("Функція f", f"{f:.3f}", f"{m_f:.3f}"))
