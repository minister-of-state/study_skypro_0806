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
Пример строки:
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
"""
