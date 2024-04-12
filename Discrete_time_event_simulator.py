import random
import numpy as np
import sys
import heapq

def gen_arrivalTime():
    return np.random.exponential(1. / float(sys.argv[1]))

def gen_departureTime():
    return np.random.exponential(1. / (1 / float(sys.argv[2])))

def select_cpu(num_cpus, scenario, idle, cpu_util_time):
    if scenario == 1:
        return random.randint(1, num_cpus)
    else:
        min_util = min(cpu_util_time)
        return cpu_util_time.index(min_util) + 1

scenario = int(sys.argv[3])
num_cpus = int(sys.argv[4])

event_q = []
ready_q = []

clock = 0.0
fin_process = 0
generated_processes = 0
num_in_ready = 0
idle = {i: 1 for i in range(1, num_cpus + 1)}
cpu_util_time = [0.0 for _ in range(num_cpus)]

# Generate the first arrival event
first_arrival_time = gen_arrivalTime()
selected_cpu = select_cpu(num_cpus, scenario, idle, cpu_util_time)
heapq.heappush(event_q, (first_arrival_time, 1, "arr", idle[selected_cpu], first_arrival_time, selected_cpu))
generated_processes += 1

while fin_process <= 9999:
    event = heapq.heappop(event_q)
    clock = event[0]
    if event[2] == "arr":
        generated_processes += 1
        arrival_time = gen_arrivalTime() + clock
        selected_cpu = select_cpu(num_cpus, scenario, idle, cpu_util_time)
        heapq.heappush(event_q, (arrival_time, generated_processes, "arr", idle[selected_cpu], arrival_time, selected_cpu))
        if idle[event[5]]:
            departure_time = gen_departureTime() + clock
            heapq.heappush(event_q, (departure_time, event[1], "dep", idle[event[5]], event[4], event[5], clock))
            idle[event[5]] = 0
        else:
            ready_q.append((event[1], "arr", idle[event[5]], event[4], event[5]))
    elif event[2] == "dep":
        fin_process += 1
        cpu_util_time[event[5] - 1] += event[0] - event[6]
        if ready_q:
            next_process = None
            for i, process in enumerate(ready_q):
                if process[4] == event[5]:
                    next_process = process
                    ready_q.pop(i)
                    break
            if next_process:
                departure_time = gen_departureTime() + clock
                heapq.heappush(event_q, (departure_time, next_process[0], "dep", idle[next_process[4]], next_process[3], next_process[4], clock))
                num_in_ready += len(ready_q)
            else:
                idle[event[5]] = 1
        else:
            idle[event[5]] = 1

print('Simulation complete!')

# Calculate performance metrics
average_turnaround_time = sum([event[4] for event in event_q if event[2] == "dep"]) / fin_process
total_throughput = fin_process / clock
average_num_in_ready = num_in_ready / fin_process
cpu_utilization = [util_time / clock for util_time in cpu_util_time]

# Print performance metrics
print("Average turnaround time: {:.4f}".format(average_turnaround_time))
print("Total throughput: {:.2f}".format(total_throughput))
print("Average number of processes in the Ready queue: {:.2f}".format(average_num_in_ready))
for i, util in enumerate(cpu_utilization):
    print("CPU {} utilization: {:.2f}".format(i + 1, util))



