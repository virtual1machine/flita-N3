import random
from random import randint
import time

DataFile = open("C://Users//natal//PycharmProjects//flita5//data.txt", "w")
testsAmount = 20
n = 1
time_list = []
while n < 25001:
    print(str(n-1)+"...Done")
    avgTime = 0
    for i in range(1, testsAmount):
        vertex_num = n
        degree = randint(0, vertex_num//2)
        graph = {}  # dictionary with vertices and their adjacent edges
        for i in range(0, vertex_num):  # giving every vertex edges
            adj_list = []
            for j in range(0, vertex_num):
                if (i != j and random.randrange(0, 1000) < 100):
                    adj_list.append(j)
            graph[i] = adj_list

        stime = time.process_time()
        found_v = []
        visited = []
        queue = []
        start_node = 0
        visited.append(start_node)
        queue.append(start_node)

        while queue:  # while length of queue is not 0 - loop
            m = queue.pop(0)

            if len(graph[m]) == degree:
                found_v.append(m)

            for neigh_v in graph[m]:
                if neigh_v not in visited:
                    visited.append(neigh_v)
                    queue.append(neigh_v)
        etime = time.process_time()
        res = (etime - stime)
        avgTime += res
    avgTime = avgTime/testsAmount
    time_list.append(avgTime)
    DataFile.write(str(n - 1))
    DataFile.write(' ')
    DataFile.write(str(avgTime))
    DataFile.write('\n')
    n += 500
DataFile.close()
