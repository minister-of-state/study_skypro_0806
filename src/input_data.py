import json
from pathlib import Path
from typing import Any

REQUIRED_KEYS = {"state", "date", "from", "to", "operationAmount"}


def validate_data(data: list[dict[str, Any]]) -> bool:
    for i, item in enumerate(data):
        missing = REQUIRED_KEYS - item.keys()
        if missing:
            print(f"Пропущены поля {missing} в элементе №{i}")
            return False
    return True


def get_data_from_user() -> list[dict[str, Any]]:
    """
    Получает данные от пользователя: ввод с клавиатуры или из файла.
    Возвращает список словарей, если структура верна.
    """
    raw_input = input("Вставьте JSON-список \
                      (или нажмите Enter, чтобы выбрать файл):\n").strip()

    if raw_input:
        try:
            data = json.loads(raw_input)
            if validate_data(data):
                return data
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
    else:
        choice = input("Нет ввода. Импортировать из файла?\
                        (y/n): ").strip().lower()
        if choice == "y":
            file_path = input("Укажите путь к файлу \
                              (например, \
                              data/input_data_examples.json): ").strip()
            path = Path(file_path)
            if path.exists():
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                    if validate_data(data):
                        return data
                except Exception as e:
                    print(f"Ошибка чтения файла: {e}")
            else:
                print("Файл не найден.")
    print("Данные не были загружены.")
    return []
