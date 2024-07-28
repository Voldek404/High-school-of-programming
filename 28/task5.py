def SynchronizingTables(N, ids, salary):
    sorted_indices_ids = sorted(range(N), key=lambda i: (ids[i], i))
    sorted_indices_salary = sorted(range(N), key=lambda i: (salary[i], i))
    salary_sorted = sorted(salary)
    salary_new = []

    for i in range(0,N):
        for j in range(0,N):
            if sorted_indices_ids[i] == sorted_indices_salary[j]:
                salary_new.append(salary[i-1])

    return salary_new
