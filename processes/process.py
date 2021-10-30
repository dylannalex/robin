class Process:
    def __init__(self, name, arrival_time, total_executions):
        self.name = name
        self.arrival_time = arrival_time
        self.total_executions = total_executions
        self.finish_time = 0
        self.executions = 0
        self.wait_time = 0

    def has_finished(self) -> bool:
        if self.executions == self.total_executions:
            return True
        return False

    def execute(self) -> None:
        self.executions += 1


def sort_processes_by_arrival_time(processes: list[Process]):
    """
    sorts a given a list of Process instances by the arrival
    time of the processes
    """
    return sorted(processes, key=lambda p: p.arrival_time)


def get_new_processes(time, processes: list[Process]):
    """
    Returns a list of the processes which arrival_time is the
    same as the given time
    """
    return [p for p in processes if p.arrival_time == time]


def get_processes_names(processes: list[Process]):
    return [process.name for process in processes]


def swap_processes(processes: list[Process], i, j):
    """
    swaps the process at index i with the process at index j
    """
    processes[i], processes[j] = processes[j], processes[i]
