# Автор: студент направления 38.03.05 «Бизнес-информатика»
# Дата: 2026
# Описание: Модуль 2 — условные конструкции и циклы

# ── Упражнение 1. Финансовый результат периода ─────────────────────────────
print("=== Финансовый результат периода ===")
monthly_profit = float(input("Введите итоговую прибыль за месяц (руб.): "))

if monthly_profit > 0:
    print("Результат: Прибыль")
elif monthly_profit < 0:
    print("Результат: Убыток")
else:
    print("Результат: Безубыточность")

# ── Упражнение 2. Классификация субъекта по выручке ────────────────────────
print("\n=== Классификация субъекта по выручке ===")
annual_revenue = float(input("Введите годовую выручку предприятия (руб.): "))

if annual_revenue <= 1_000_000:
    category = "Микробизнес"
elif annual_revenue <= 10_000_000:
    category = "Малый бизнес"
elif annual_revenue <= 100_000_000:
    category = "Средний бизнес"
else:
    category = "Крупный бизнес"
print(f"Категория предприятия: {category}")

# ── Упражнение 3. Расчёт НДФЛ ──────────────────────────────────────────────
print("\n=== Расчёт налога на доходы физических лиц ===")
monthly_salary = float(input("Введите ежемесячную заработную плату (руб.): "))

ndfl_rate = 0.13 if monthly_salary <= 50_000 else 0.15
tax_amount = monthly_salary * ndfl_rate
net_salary = monthly_salary - tax_amount
print(f"Ставка НДФЛ:    {int(ndfl_rate * 100)}%")
print(f"Сумма налога:   {tax_amount:.2f} руб.")
print(f"Зарплата на руки: {net_salary:.2f} руб.")

# ── Упражнение 6. Накопление капитала по модели сложного процента ───────────
print("\n=== Накопление капитала (сложный процент) ===")
initial_capital = float(input("Введите начальный капитал (руб.): "))
interest_rate = float(input("Введите процентную ставку (% годовых): "))

print(f"\n{'Год':<6} {'Накопленная сумма':>20}")
print("-" * 28)
for year in range(1, 6):
    accumulated = initial_capital * (1 + interest_rate / 100) ** year
    print(f"{year:<6} {accumulated:>19.2f} руб.")

# ── Упражнение 9. Анализ выручки за полугодие ──────────────────────────────
print("\n=== Анализ выручки за полугодие ===")
revenues = []
for month in range(1, 7):
    value = float(input(f"Выручка за месяц {month} (руб.): "))
    revenues.append(value)

print(f"\nМинимальная выручка:    {min(revenues):.2f} руб.")
print(f"Максимальная выручка:   {max(revenues):.2f} руб.")
print(f"Среднемесячная выручка: {sum(revenues) / len(revenues):.2f} руб.")
