import math

# Вихідні дані (Варіант 4)
heights = [53.643, 53.650, 53.664, 53.655, 53.661, 53.649]  # метри
std_devs_mm = [5.4, 4.7, 11.1, 8.4, 9.7, 3.5]  # мм

n = len(heights)
lambda_coeff = 100  # Коефіцієнт пропорційності для ваг

# 1. Обчислення ваг
weights = []
sq_std_devs = []
print("1. Обчислення ваг (λ = 100):")
print("-" * 30)
print("| № | m (мм) | m^2    | p = λ/m^2 |")
print("|---|--------|--------|-----------|")
sum_p = 0
for i in range(n):
    m_sq = std_devs_mm[i]**2
    p = lambda_coeff / m_sq
    weights.append(p)
    sq_std_devs.append(m_sq)
    sum_p += p
    print(f"| {i+1:<2}| {std_devs_mm[i]:<6} | {m_sq:<6.2f} | {p:<9.2f} |")
print(f"| Сума |        |        | {sum_p:<9.2f} |")
print("-" * 30)

# 2. Обчислення середньовагового значення L0
l0 = heights[0]  # Наближене значення
print(f"\n2. Обчислення середньовагового значення L0 (l0 = {l0} м):")
print("-" * 60)
print("| № | H (м)   | p     | ε (мм) | p*ε     | p*ε^2    |")
print("|---|---------|-------|--------|---------|----------|")
sum_pe = 0
sum_pe2 = 0
epsilons_mm = []
for i in range(n):
    epsilon_m = heights[i] - l0
    epsilon_mm = round(epsilon_m * 1000) # Working with mm for epsilons
    epsilons_mm.append(epsilon_mm)
    pe = weights[i] * epsilon_mm
    pe2 = weights[i] * epsilon_mm**2
    sum_pe += pe
    sum_pe2 += pe2
    print(f"| {i+1:<2}| {heights[i]:<7.3f} | {weights[i]:<5.2f} | {epsilon_mm:<6} | {pe:<7.2f} | {pe2:<8.2f} |")
print(f"| Сума |         | {sum_p:<5.2f} |        | {sum_pe:<7.2f} | {sum_pe2:<8.2f} |")
print("-" * 60)

l0_weighted = l0 + (sum_pe / sum_p) / 1000
print(f"   L0 = {l0} + ({sum_pe:.2f} / {sum_p:.2f}) / 1000 = {l0_weighted:.5f} м")

# 3 & 4. Обчислення відхилень δ та СКП одиниці ваги μ
print("\n3 & 4. Обчислення δ та СКП одиниці ваги μ:")
print("-" * 40)
print("| № | H (м)   | L0 (м)  | δ (мм) | p     | p*δ^2   |")
print("|---|---------|---------|--------|-------|---------|")
sum_pd2 = 0
deltas_mm = []
for i in range(n):
    delta_m = heights[i] - l0_weighted
    delta_mm = delta_m * 1000 # Keep precision for calculation
    deltas_mm.append(delta_mm)
    pd2 = weights[i] * delta_mm**2
    sum_pd2 += pd2
    print(f"| {i+1:<2}| {heights[i]:<7.3f} | {l0_weighted:<7.5f} | {delta_mm:<6.1f} | {weights[i]:<5.2f} | {pd2:<7.2f} |")
print(f"| Сума |         |         |        |       | {sum_pd2:<7.2f} |")
print("-" * 40)

mu = math.sqrt(sum_pd2 / (n - 1))
print(f"   μ = sqrt([{sum_pd2:.2f}] / {n-1}) = {mu:.2f} мм")

# 5. Контроль обчислень
control_pd2 = sum_pe2 - (sum_pe**2 / sum_p)
control_mu = math.sqrt(lambda_coeff)
print("\n5. Контроль обчислень:")
print(f"   Контроль [pδ^2]: {sum_pd2:.2f}")
print(f"   Контроль [pε^2] - [pε]^2/[p]: {sum_pe2:.2f} - ({sum_pe:.2f})^2 / {sum_p:.2f} = {control_pd2:.2f}")
print(f"   Контроль μ ≈ sqrt(λ): {mu:.2f} ≈ {control_mu:.2f}")

# 6. Обчислення СКП середньовагового значення M
M = mu / math.sqrt(sum_p)
print(f"\n6. СКП середньовагового значення M = μ / sqrt([p]) = {mu:.2f} / sqrt({sum_p:.2f}) = {M:.2f} мм")

print(f"\nОстаточний результат: H_A = {l0_weighted:.4f} ± {M/1000:.4f} м")