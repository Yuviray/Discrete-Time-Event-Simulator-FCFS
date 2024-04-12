# Discrete-Time-Event-Simulator-FCFS
This Discrete Time Event Simulator (FCFS) was designed in order to
assess the impact of different workloads on the following performance metrics.

- The average turnaround time of processes
- The total throughput (number of processes done per unit time)
- The CPU utilization
- The average number of processes in the Ready queue

This time the simulator will be adapted to handle 2 scenarios:

Scenario 1: Every CPU has its own Ready Queue. When a process arrives, it selects one of the
CPUs uniformly at random (e.g., if we have 4 CPUs, a process would select a particular CPU with
probability 0.25).

Scenario 2: All CPUs share a global Ready Queue. When a process arrives and none of the CPUs
are available, it joins the Ready Queue. Once a CPU becomes available, it would dispatch a
process from the Ready Queue

Program run commands:
 $ python Discrete_time_event_simulator.py 20 0.04 1 4
 
 Enter the file name and the arrival rate and the average service
 times the scenario in which the simulation needs to run and the
 number of CPUs

A report with the finding is provided
