#Студент: Гаврилов Кирилл Алексеевич
#Группа: БИЗ-Б-0-Д-2024-1
#Дата: 15.06.2026
# Описание: Модуль 3 — функции

# ── Упражнение 1. calculate_profit() ───────────────────────────────────────
def calculate_profit(revenue: float, costs: float) -> float:
    """Вычисляет прибыль как разность выручки и затрат.

    Args:
        revenue: Выручка предприятия в рублях.
        costs:   Общие затраты предприятия в рублях.

    Returns:
        Величина прибыли (может быть отрицательной при убытке).
    """
    return revenue - costs


print("=== calculate_profit() ===")
print(f"Набор 1: {calculate_profit(500_000, 320_000):.2f} руб.")
print(f"Набор 2: {calculate_profit(1_200_000, 980_000):.2f} руб.")
print(f"Набор 3: {calculate_profit(750_000, 800_000):.2f} руб.")


# ── Упражнение 2. calculate_vat() ──────────────────────────────────────────
def calculate_vat(price: float, vat_rate: float = 20.0) -> float:
    """Вычисляет сумму НДС для указанной цены.

    Args:
        price:    Цена товара в рублях.
        vat_rate: Ставка НДС в процентах (по умолчанию 20%).

    Returns:
        Сумма НДС в рублях.
    """
    return price * (vat_rate / 100)


print("\n=== calculate_vat() ===")
print(f"НДС 10% от 5 000 руб.:  {calculate_vat(5000, 10):.2f} руб.")
print(f"НДС 20% от 5 000 руб.:  {calculate_vat(5000):.2f} руб.")


# ── Упражнение 3. get_business_category() ──────────────────────────────────
def get_business_category(annual_revenue: float) -> str:
    """Возвращает категорию бизнеса по годовой выручке.

    Args:
        annual_revenue: Годовая выручка предприятия в рублях.

    Returns:
        Строка с категорией: 'Микробизнес', 'Малый бизнес',
        'Средний бизнес' или 'Крупный бизнес'.
    """
    if annual_revenue <= 1_000_000:
        return "Микробизнес"
    elif annual_revenue <= 10_000_000:
        return "Малый бизнес"
    elif annual_revenue <= 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"


print("\n=== get_business_category() ===")
for test_revenue in [500_000, 7_000_000, 55_000_000, 250_000_000]:
    print(f"{test_revenue:>15,.0f} руб. → {get_business_category(test_revenue)}")


# ── Упражнение 4. compound_interest() ──────────────────────────────────────
def compound_interest(principal: float, rate: float, years: int) -> float:
    """Вычисляет итоговую сумму по формуле сложного процента.

    Args:
        principal: Начальный капитал в рублях.
        rate:      Годовая процентная ставка в процентах.
        years:     Срок инвестирования в годах.

    Returns:
        Итоговая сумма накоплений в рублях.
    """
    return principal * (1 + rate / 100) ** years


print("\n=== compound_interest() ===")
start_capital = 100_000
annual_rate = 10.0
for term in [3, 5, 10]:
    result = compound_interest(start_capital, annual_rate, term)
    print(f"Срок {term:>2} лет: {result:>12,.2f} руб.")


# ── Упражнение 7. payback_period() ─────────────────────────────────────────
def payback_period(investment: float, annual_profit: float) -> str:
    """Вычисляет срок окупаемости инвестиционного проекта.

    Args:
        investment:    Объём первоначальных инвестиций в рублях.
        annual_profit: Ожидаемая годовая прибыль в рублях.

    Returns:
        Строка с результатом расчёта или сообщение об ошибке.
    """
    if annual_profit <= 0:
        return "Расчёт невозможен: прибыль должна быть положительной"
    period = investment / annual_profit
    return f"{period:.2f} лет"


print("\n=== payback_period() ===")
print(f"Инвестиции 500 000, прибыль 125 000/год → {payback_period(500_000, 125_000)}")
print(f"Инвестиции 1 000 000, прибыль 0/год    → {payback_period(1_000_000, 0)}")
print(f"Инвестиции 300 000, прибыль -50 000/год → {payback_period(300_000, -50_000)}")
