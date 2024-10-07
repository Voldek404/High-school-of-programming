import time
import random
from threading import Thread


def arraySumByBlocks(process_id, rawList, start, end, res):
    local_sum = 0
    for i in range(start, end):
        local_sum += rawList[i]
    res[process_id] = local_sum


rawList = []
res = {}
numberOfProcesses = 5
list_size = 10000
block_size = list_size // numberOfProcesses
for i in range(list_size):
    rawList.append(random.uniform(0, 100))
threads = []
for process_id in range(numberOfProcesses):
    start = process_id * block_size
    end = (process_id + 1) * block_size if process_id != numberOfProcesses - 1 else list_size
    t = Thread(target=arraySumByBlocks, args=(process_id, rawList, start, end, res))
    threads.append(t)
    t.start()
total_sum = sum(res.values())


