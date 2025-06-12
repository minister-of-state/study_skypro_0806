from datetime import datetime
from src.masks import mask_card, mask_account
from src.processing import filter_by_state, sort_by_date


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счёта.
    :param info: строка, содержащая тип и номер
    (например, 'Visa Platinum 7000792289606361')
    :return: замаскированная строка
    """
    if info.startswith("Счет"):
        return f"Счет {mask_account(info.split()[-1])}"
    else:
        parts = info.rsplit(' ', 1)
        card_type = parts[0]
        card_number = parts[1]
        return f"{card_type} {mask_card(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.
    :param date_str: строка даты в формате
    "2024-03-11T02:26:18.671407"
    :return: строка в формате "11.03.2024"
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


def demo_filter_by_state():
    """
    Демонстрация работы filter_by_state.
    Можно заменить input() на реальные данные или тестовый список.
    """
    data = input()
    result = filter_by_state(data, state='EXECUTED')
    return result


def demo_sort_by_date():
    """
    Демонстрация работы sort_by_date.
    """
    date_info = input()

    result = sort_by_date(date_info, reverse=True)
    # По убыванию (сначала последние)
    return result
