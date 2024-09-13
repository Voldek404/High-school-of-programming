import json
import requests


def jsonOperations():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    user_data = {}
    for item in todos:
        user_id = item['userId']
        task_id = item['id']
        completed = item['completed']
        if user_id not in user_data:
            user_data[user_id] = {'unique_tasks': set(), 'completed_tasks': 0}
        user_data[user_id]['unique_tasks'].add(task_id)
        if completed:
            user_data[user_id]['completed_tasks'] += 1
    result = {}
    for user_id, data in user_data.items():
        result[user_id] = {'unique_tasks_count': len(data['unique_tasks']),
                           'completed_tasks_count': data['completed_tasks']}
    return result
