def SynchronizingTables(N, ids, salary):
    sorted_indices_ids = sorted(range(N), key=lambda i: (ids[i], i))
    sorted_indices_salary = sorted(range(N), key=lambda i: (salary[i], i))
    salary_sorted = sorted(salary)
    salary_new = []

    for j in sorted_indices_ids:
        for i in sorted_indices_salary:
            if i == j:
                salary_new.append(salary_sorted[j])

    return salary_new
