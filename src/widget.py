from datetime import datetime
from masks import mask_card, mask_account


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
