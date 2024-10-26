import queue

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin(processes, quantum):
    time = 0
    ready_queue = queue.Queue()
    for process in processes:
        ready_queue.put(process)
    
    gantt_chart = []
    
    while not ready_queue.empty():
        current_process = ready_queue.get()
        
        if current_process.remaining_time <= quantum:
            time += current_process.remaining_time
            gantt_chart.append((current_process.pid, time))
            current_process.turnaround_time = time
            current_process.remaining_time = 0
        else:
            time += quantum
            gantt_chart.append((current_process.pid, time))
            current_process.remaining_time -= quantum
            ready_queue.put(current_process)
    
    for process in processes:
        process.waiting_time = process.turnaround_time - process.burst_time
    
    return gantt_chart

def shortest_job_first(processes):
    processes.sort(key=lambda x: x.burst_time)
    time = 0
    gantt_chart = []
    
    for process in processes:
        time += process.burst_time
        gantt_chart.append((process.pid, time))
        process.turnaround_time = time
        process.waiting_time = process.turnaround_time - process.burst_time
    
    return gantt_chart

def calculate_average_times(processes):
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    return avg_waiting_time, avg_turnaround_time

def print_gantt_chart(gantt_chart):
    print("Gantt Chart:")
    for pid, end_time in gantt_chart:
        print(f"|  P{pid}  ", end="")
    print("|")
    print("0", end="")
    for _, end_time in gantt_chart:
        print(f"      {end_time}", end="")
    print()

def get_user_input():
    processes = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process P{i+1}: "))
        processes.append(Process(i+1, burst_time))
    return processes

def main():
    processes = get_user_input()
    

    quantum = int(input("Enter time quantum for Round Robin: "))
    print("\nRound Robin Scheduling:")
    processes_rr = [Process(p.pid, p.burst_time) for p in processes]  
    gantt_chart_rr = round_robin(processes_rr, quantum)
    print_gantt_chart(gantt_chart_rr)
    avg_waiting_time_rr, avg_turnaround_time_rr = calculate_average_times(processes_rr)
    print(f"Average Waiting Time: {avg_waiting_time_rr:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time_rr:.2f}")
    
    print("\n" + "="*50 + "\n")
    
    print("Shortest Job First Scheduling:")
    processes_sjf = [Process(p.pid, p.burst_time) for p in processes]  
    gantt_chart_sjf = shortest_job_first(processes_sjf)
    print_gantt_chart(gantt_chart_sjf)
    avg_waiting_time_sjf, avg_turnaround_time_sjf = calculate_average_times(processes_sjf)
    print(f"Average Waiting Time: {avg_waiting_time_sjf:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time_sjf:.2f}")

if __name__ == "__main__":
    main()