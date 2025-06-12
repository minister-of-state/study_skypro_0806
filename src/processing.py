from datetime import datetime


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей, содержащих
    данные с ключом 'state'.

    :param state: Значение для фильтрации
    по ключу 'state' (по умолчанию 'EXECUTED').

    :return: Новый список, содержащий только
    словари с указанным значением 'state'.
    """
    return [item for item in data if item.get("state") == state]


"""
Пример строки для filter_by_state:
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
"""


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data: Список словарей с ключом 'date' в ISO формате.

    :param reverse: Порядок сортировки.
    True — по убыванию (сначала самые последние).

    :return: Новый отсортированный список словарей.
    """
    return sorted(
        data,
        key=lambda item: datetime.fromisoformat(item.get("date", "")),
        reverse=reverse
    )


"""
Пример использования sort_by_date:
sorted_data = sort_by_date(data)  # По убыванию (reverse=True)
sorted_data_asc = sort_by_date(data, reverse=False)  # По возрастанию
"""
