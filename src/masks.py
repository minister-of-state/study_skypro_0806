def mask_card(number: str) -> str:
    """
    Маскирует номер карты. Пример: 7000 79** **** 6361
    """
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account(number: str) -> str:
    """
    Маскирует номер счёта. Пример: **4305
    """
    return f"**{number[-4:]}"
