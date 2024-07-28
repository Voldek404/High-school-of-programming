def SynchronizingTables(N, ids, salary):
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)

    ids_salary_dict = {id: salary for id, salary in zip(sorted_ids, sorted_salary)}
    new_salary = [id_salary_map[id] for id in ids]

    return new_salary
