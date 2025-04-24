import math
import numpy as np

# Вихідні дані для варіанту 4
measurements_sec = np.array([29, 33, 34, 35, 30, 34, 32, 31, 31, 33])
n = len(measurements_sec)

# 1. Надійне значення
L0_sec = np.mean(measurements_sec)
L0_deg = 115
L0_min = 27
L0_total_sec = L0_deg * 3600 + L0_min * 60 + L0_sec

print("="*50)
print("1. Надійне значення виміряної величини (L₀):")
print(f"   Середнє значення: {L0_sec:.1f}''")
print(f"   Кут: {L0_deg}° {L0_min}' {L0_sec:.1f}''")
print("="*50)

# 2. Надійні похибки
delta_i = measurements_sec - L0_sec
sum_delta_i = np.sum(delta_i)

print("2. Надійні похибки (δᵢ):")
print(f"   δᵢ = {np.round(delta_i, 2)}")
print(f"   Контроль суми похибок: ∑δᵢ = {sum_delta_i:.2f}")
print("="*50)

# 3. Сума квадратів похибок
delta_i_sq = delta_i**2
sum_delta_i_sq = np.sum(delta_i_sq)

# Контроль за формулою (10.9)
l0_approx = np.min(measurements_sec)
epsilon_i = measurements_sec - l0_approx
sum_epsilon_i = np.sum(epsilon_i)
sum_epsilon_i_sq = np.sum(epsilon_i**2)
control_sum_delta_sq = sum_epsilon_i_sq - (sum_epsilon_i**2) / n

print("3. Сума квадратів надійних похибок ([δ²]):")
print(f"   δᵢ² = {np.round(delta_i_sq, 2)}")
print(f"   ∑δᵢ² = {sum_delta_i_sq:.2f}")
print(f"   Контроль за формулою (10.9): {control_sum_delta_sq:.2f}")
print("="*50)

# 4. СКП одного виміру
if n > 1:
    m = math.sqrt(sum_delta_i_sq / (n - 1))
    print("4. Середньоквадратична похибка одного виміру (m):")
    print(f"   m = ±√({sum_delta_i_sq:.2f} / ({n} - 1)) = ±{m:.2f}''")
else:
    m = float('nan')
    print("4. Середньоквадратична похибка одного виміру (m): Неможливо обчислити (n=1)")
print("="*50)

# 5. СКП надійного значення
if not math.isnan(m):
    M = m / math.sqrt(n)
    print("5. Середньоквадратична похибка середнього (M):")
    print(f"   M = ±({m:.2f}'' / √{n}) = ±{M:.2f}''")
else:
    M = float('nan')
    print("5. Середньоквадратична похибка середнього (M): Неможливо обчислити")
print("="*50)

# 6. Остаточний результат
print("6. Остаточний результат:")
if not math.isnan(M):
    print(f"   L₀ ± M = {L0_deg}° {L0_min}' {L0_sec:.1f}'' ± {M:.2f}''")
else:
    print("   Неможливо представити остаточний результат.")
print("="*50)
