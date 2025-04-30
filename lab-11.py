import math

# Вихідні дані (Варіант 4) в метрах
direct_measurements = [671.890, 356.445, 67.560, 512.985, 359.380, 274.091, 783.892, 330.011, 489.096, 178.044]
reverse_measurements = [671.955, 356.522, 67.661, 512.980, 359.280, 274.145, 783.854, 330.074, 489.147, 178.095]

n = len(direct_measurements)
differences_mm = []
abs_differences_mm = []
sq_differences_mm2 = []

# 1. Обчислення різниць
print("1. Обчислення різниць:")
print("-" * 30)
print("| № | Прямий (м) | Зворотний (м) | d (мм) | |d| (мм) | d^2 (мм^2) |")
print("|---|------------|---------------|--------|---------|------------|")
sum_d = 0
sum_abs_d = 0
sum_sq_d = 0
for i in range(n):
    d_m = direct_measurements[i] - reverse_measurements[i]
    d_mm = round(d_m * 1000)
    abs_d_mm = abs(d_mm)
    sq_d_mm2 = d_mm**2
    differences_mm.append(d_mm)
    abs_differences_mm.append(abs_d_mm)
    sq_differences_mm2.append(sq_d_mm2)
    sum_d += d_mm
    sum_abs_d += abs_d_mm
    sum_sq_d += sq_d_mm2
    print(f"| {i+1:<2}| {direct_measurements[i]:<10.3f} | {reverse_measurements[i]:<13.3f} | {d_mm:<6} | {abs_d_mm:<7} | {sq_d_mm2:<10} |")
print("| Сума |            |               | {sum_d:<6} | {sum_abs_d:<7} | {sum_sq_d:<10} |".format(sum_d=sum_d, sum_abs_d=sum_abs_d, sum_sq_d=sum_sq_d))
print("-" * 30)

# 2. Перевірка на систематичні похибки
print("\n2. Перевірка на систематичні похибки:")
systematic_error_threshold = 0.25 * sum_abs_d
print(f"   Сума різниць [d]: {sum_d} мм")
print(f"   Сума модулів різниць [|d|]: {sum_abs_d} мм")
print(f"   Критерій: |[d]| <= 0.25 * [|d|]")
print(f"   |{sum_d}| <= 0.25 * {sum_abs_d}")
print(f"   {abs(sum_d)} <= {systematic_error_threshold:.2f}")

systematic_errors_present = abs(sum_d) > systematic_error_threshold

if systematic_errors_present:
    print("   Нерівність НЕ виконується. Систематичні похибки присутні.")

    # 3. Визначення величини систематичного впливу (d0)
    d0 = sum_d / n
    print(f"\n3. Величина систематичного впливу d0 = {d0:.1f} мм")

    # 4. Вилучення систематичного впливу
    print("\n4. Вилучення систематичного впливу та обчислення виправлених різниць (Δd):")
    print("-" * 40)
    print("| № | d (мм) | d0 (мм) | Δd (мм) | Δd^2 (мм^2) |")
    print("|---|--------|---------|---------|-------------|")
    corrected_differences_mm = []
    sq_corrected_differences_mm2 = []
    sum_delta_d = 0
    sum_sq_delta_d = 0
    for i in range(n):
        delta_d = differences_mm[i] - d0
        sq_delta_d = delta_d**2
        corrected_differences_mm.append(delta_d)
        sq_corrected_differences_mm2.append(sq_delta_d)
        sum_delta_d += delta_d
        sum_sq_delta_d += sq_delta_d
        print(f"| {i+1:<2}| {differences_mm[i]:<6} | {d0:<7.1f} | {delta_d:<7.1f} | {sq_delta_d:<11.2f} |")
    print(f"| Сума |        |         | {sum_delta_d:<7.1f} | {sum_sq_delta_d:<11.2f} |")
    print("-" * 40)
    print(f"   Контроль: [Δd] = {sum_delta_d:.1f} (має бути близьким до 0)")

    # 5. Обчислення СКП однієї виправленої різниці (m_delta_d) за формулою Бесселя
    m_delta_d = math.sqrt(sum_sq_delta_d / (n - 1))
    print(f"\n5. СКП однієї виправленої різниці m_Δd = sqrt({sum_sq_delta_d:.1f} / {n-1}) = {m_delta_d:.2f} мм")

    # 6. Обчислення СКП одного виміру (m)
    m = m_delta_d / math.sqrt(2)
    print(f"\n6. СКП одного виміру m = m_Δd / sqrt(2) = {m:.2f} мм")

    # 7. Обчислення СКП середнього значення (m_ser)
    m_ser = m_delta_d / 2 # Corrected based on derivation
    print(f"\n7. СКП середнього значення m_сер = m_Δd / 2 = {m_ser:.2f} мм")

else:
    print("   Нерівність виконується. Систематичні похибки відсутні.")
    # 3.1 Обчислення СКП однієї різниці (md) за формулою Гаусса
    m_d = math.sqrt(sum_sq_d / n)
    print(f"\n3.1 СКП однієї різниці m_d = sqrt([{sum_sq_d}] / {n}) = {m_d:.2f} мм")

    # 4.1 СКП одного виміру (m)
    m = m_d / math.sqrt(2)
    print(f"\n4.1 СКП одного виміру m = m_d / sqrt(2) = {m:.2f} мм")

    # 5.1 СКП середнього значення (m_ser)
    m_ser = m / math.sqrt(2) # m_ser = m_d / 2
    print(f"\n5.1 СКП середнього значення m_сер = m / sqrt(2) = {m_ser:.2f} мм")

print("\nРозрахунки завершено.")