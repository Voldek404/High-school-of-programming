import json
import requests


def jsonOperations():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    result = json.loads(response.text)
    unique_users = {item['userId'] for item in result if 'userId' in item}
    unique_tasks = {item['id'] for item in result if 'id' in item}
    countTrueTasks = sum(1 for item in result if item.get('completed') == True)
    unique_ids = f"Количество уникальных пользователей: {len(unique_users)}"
    unique_tasks = f"Количество уникальных задач: {len(unique_tasks)}"
    done_tasks = f"Количество выполненных задач: {countTrueTasks}"
    return unique_ids, unique_tasks, done_tasks
