#Студент: Гаврилов Кирилл Алексеевич
#Группа: БИЗ-Б-0-Д-2024-1
#Дата: 15.06.2026
# Описание: Мини-проект — Вариант 10. Анализ и актуализация прайс-листа

def get_price_list(min_items: int = 5, max_items: int = 7) -> list[dict]:
    """Запрашивает у пользователя товары и их цены.

    Args:
        min_items: Минимальное количество позиций прайс-листа.
        max_items: Максимальное количество позиций прайс-листа.

    Returns:
        Список словарей с ключами 'name' и 'price'.
    """
    print(f"Введите от {min_items} до {max_items} позиций прайс-листа.")
    items = []
    for i in range(1, max_items + 1):
        name = input(f"  Позиция {i} — наименование (или Enter для завершения): ").strip()
        if not name:
            if i <= min_items:
                print(f"  Необходимо ввести минимум {min_items} позиции. Продолжайте.")
                name = input(f"  Позиция {i} — наименование: ").strip()
            else:
                break
        price_str = input(f"  Позиция {i} — цена (руб.): ")
        items.append({"name": name, "price": float(price_str)})
    return items


def calculate_average_price(items: list[dict]) -> float:
    """Вычисляет среднюю цену по прайс-листу.

    Args:
        items: Список товаров с ценами.

    Returns:
        Средняя цена в рублях.
    """
    total = sum(item["price"] for item in items)
    return total / len(items)


def find_extreme_items(items: list[dict]) -> tuple[dict, dict]:
    """Находит самый дорогой и самый дешёвый товар.

    Args:
        items: Список товаров с ценами.

    Returns:
        Кортеж (самый_дорогой, самый_дешёвый).
    """
    most_expensive = max(items, key=lambda item: item["price"])
    cheapest = min(items, key=lambda item: item["price"])
    return most_expensive, cheapest


def apply_markup(items: list[dict], markup_percent: float = 15.0) -> list[dict]:
    """Применяет наценку ко всем позициям прайс-листа.

    Args:
        items:          Список товаров с исходными ценами.
        markup_percent: Процент наценки (по умолчанию 15%).

    Returns:
        Новый список товаров с обновлёнными ценами.
    """
    coefficient = 1 + markup_percent / 100
    return [{"name": item["name"], "price": round(item["price"] * coefficient, 2)}
            for item in items]


def print_price_list(items: list[dict], title: str = "Прайс-лист") -> None:
    """Выводит прайс-лист в табличном формате.

    Args:
        items: Список товаров с ценами.
        title: Заголовок таблицы.
    """
    print(f"\n{'─' * 45}")
    print(f"  {title}")
    print(f"{'─' * 45}")
    print(f"  {'№':<4} {'Наименование':<25} {'Цена':>10}")
    print(f"{'─' * 45}")
    for i, item in enumerate(items, start=1):
        print(f"  {i:<4} {item['name']:<25} {item['price']:>9.2f} руб.")
    print(f"{'─' * 45}")


# ── Главная программа ───────────────────────────────────────────────────────
print("╔══════════════════════════════════════════╗")
print("║  Анализ и актуализация прайс-листа       ║")
print("╚══════════════════════════════════════════╝\n")

# Ввод данных
price_list = get_price_list()

# Вывод исходного прайс-листа
print_price_list(price_list, "Исходный прайс-лист")

# Анализ
avg_price = calculate_average_price(price_list)
most_expensive, cheapest = find_extreme_items(price_list)
above_avg_count = sum(1 for item in price_list if item["price"] > avg_price)

print(f"\n Аналитика:")
print(f"  Средняя цена:             {avg_price:.2f} руб.")
print(f"  Самый дорогой товар:      {most_expensive['name']} — {most_expensive['price']:.2f} руб.")
print(f"  Самый дешёвый товар:      {cheapest['name']} — {cheapest['price']:.2f} руб.")
print(f"  Позиций выше средней цены: {above_avg_count} из {len(price_list)}")

# Актуализация прайс-листа с наценкой 15%
markup = 15.0
updated_price_list = apply_markup(price_list, markup)
print_price_list(updated_price_list, f"Обновлённый прайс-лист (наценка +{markup:.0f}%)")
