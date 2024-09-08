import json
import requests


def jsonOperations():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    result = json.loads(response.text)
    with open("result.json", "w") as f:
        json.dump(result, f, indent=4)
    with open("result.json", "r") as f:
        json2 = json.load(f)
    key_to_collect = 'userId'
    combined_values = {}
    with open("result.json", "r") as f:
        for item in result:
            key_value = item.get(key_to_collect)
            if key_value is not None:
                combined_values[
                    key_value] = item  # Заполняем словарь, где ключ - это значение по ключу, а значение - весь объект
    unique_ids = f"Количество уникальных пользователей {len(combined_values)}"
    return unique_ids
