def SynchronizingTables(N, ids, salary):
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)
    new_salary = []
    ids_salary_dict = dict(zip(sorted_ids, sorted_salary))
    for i in ids:
        new_salary.append(ids_salary_dict[i])

    return new_salary
