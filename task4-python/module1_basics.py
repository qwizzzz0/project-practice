# Автор: студент направления 38.03.05 «Бизнес-информатика»
# Дата: 2026
# Описание: Модуль 1 — переменные, типы данных, ввод и вывод

# ── Упражнение 1. Карточка сотрудника ──────────────────────────────────────
employee_name: str = "Иван Петров"
employee_age: int = 28
employee_salary: float = 75000.0
is_employed: bool = True

print("=== Карточка сотрудника ===")
print(f"Имя:              {employee_name}")
print(f"Возраст:          {employee_age} лет")
print(f"Заработная плата: {employee_salary:.2f} руб.")
print(f"Трудоустроен:     {is_employed}")

# ── Упражнение 3. Расчёт итоговой стоимости ────────────────────────────────
print("\n=== Расчёт итоговой стоимости ===")
unit_price = float(input("Введите цену единицы товара (руб.): "))
quantity = int(input("Введите количество единиц: "))

total_cost = unit_price * quantity
print(f"Итоговая стоимость: {total_cost:.2f} руб.")

# ── Упражнение 4. Доход по банковскому вкладу ──────────────────────────────
print("\n=== Доход по банковскому вкладу ===")
deposit_amount = float(input("Введите сумму вклада (руб.): "))
annual_rate = float(input("Введите процентную ставку (% годовых): "))

income = deposit_amount * (annual_rate / 100)
total_with_income = deposit_amount + income
print(f"Доход за год:       {income:.2f} руб.")
print(f"Итоговая сумма:     {total_with_income:.2f} руб.")

# ── Упражнение 5. Конвертация валюты ───────────────────────────────────────
print("\n=== Конвертация валюты ===")
usd_rate = float(input("Введите курс доллара к рублю: "))
amount_rub = float(input("Введите сумму в рублях: "))

amount_usd = round(amount_rub / usd_rate, 2)
print(f"Эквивалент в долларах: {amount_usd} USD")

# ── Упражнение 6. Прибыль и рентабельность продаж ──────────────────────────
print("\n=== Прибыль и рентабельность продаж ===")
revenue = float(input("Введите выручку предприятия (руб.): "))
costs = float(input("Введите общие затраты предприятия (руб.): "))

profit = revenue - costs
profitability = (profit / revenue * 100) if revenue != 0 else 0
print(f"Прибыль:               {profit:.2f} руб.")
print(f"Рентабельность продаж: {profitability:.2f}%")
