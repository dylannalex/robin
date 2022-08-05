from operator import attrgetter


class Process:
    def __init__(self, name, arrival_time, total_executions):
        self.name = name
        self.arrival_time = arrival_time
        self.total_executions = total_executions
        self.finish_time = 0
        self.current_executions = 0
        self.consecutive_executions = 0
        self.wait_time = 0

    def execute(self) -> None:
        self.current_executions += 1
        self.consecutive_executions += 1

    def reset(self) -> None:
        self.finish_time = 0
        self.current_executions = 0
        self.consecutive_executions = 0
        self.wait_time = 0

    def execute(self) -> None:
        self.current_executions += 1

    def reset(self) -> None:
        self.finish_time = 0
        self.current_executions = 0
        self.wait_time = 0

    def has_finished(self) -> bool:
        if self.current_executions == self.total_executions:
            return True
        return False

    @property
    def remaining_executions(self):
        return self.total_executions - self.current_executions


class ProcessList:
    """
    Static class with methods to handle lists of Process objects
    """

    def parse_processes_string(
        processes_string: str,
        process_attributes_separator: str = "-",
        processes_separator: str = ",",
    ) -> list[Process]:
        """
        Parses the given processes string.

        @processes_string: process_name-arrival_time-total_executions|process_name-arrival_time-total_executions...
        @process_attributes_separator: character that separates each process attribute. Default is '-'.
        @processes_separator: character that separates each process. Default is ','.

        Example:
            parse_processes_string("A-1-5,B-2-6,C-3-8")
            >>> [Process("A", 1, 5), Process("B", 2, 6), Process("C", 3, 8)]
        """
        processes_list: list[tuple[str, str, str]] = [
            l.split(process_attributes_separator)
            for l in processes_string.split(processes_separator)
        ]
        return [Process(p[0], int(p[1]), int(p[2])) for p in processes_list]

    def sort_processes_by_arrival_time(processes: list[Process]):
        """
        Sorts a given a list of Process instances by the arrival
        time of the processes.
        """
        return sorted(processes, key=lambda p: p.arrival_time)

    def get_new_processes(time, slept_processes: list[Process]):
        """
        Returns a list of the processes which arrival_time is the
        same as the given time and updates the slept_processes list
        by removing the new processes from it.
        """
        new_processes = [p for p in slept_processes if p.arrival_time == time]
        slept_processes = [p for p in slept_processes if p not in new_processes]
        return new_processes, slept_processes

    def get_processes_names(processes: list[Process]):
        return [process.name for process in processes]

    def swap_processes(processes: list[Process], i, j):
        """
        Swaps the process at index i with the process at index j.
        """
        processes[i], processes[j] = processes[j], processes[i]

    def find_first_processes(processes: list[Process]):
        """
        Finds all the processes that arrive first.
        """
        sorted_processes = ProcessList.sort_processes_by_arrival_time(processes)
        first_arrival_time = sorted_processes[0].arrival_time
        first_processes = []
        for process in sorted_processes:
            if process.arrival_time != first_arrival_time:
                return first_processes
            first_processes.append(process)

        return first_processes

    def sort_processes_by_total_executions(processes: list[Process]):
        return sorted(processes, key=lambda p: p.total_executions)

    def sort_processes_by_remaining_executions(processes: list[Process]):
        """
        Sorts processes by their remaining current_executions. If two processes have the
        same remaining current_executions, the processes that arrives first has priority.
        """
        return sorted(processes, key=attrgetter("remaining_executions", "arrival_time"))

    def get_shortest_process(processes: list[Process]):
        return ProcessList.sort_processes_by_total_executions(processes)[0]
