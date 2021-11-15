from processes.process import *


class ExecutionsTable:
    def __init__(self):
        self.processes = []
        self.executions = []

    def add_execution(
        self, time: int, process: Process, waiting_processes: list[Process]
    ) -> None:
        self.executions.append(
            {
                "time": time,
                "process_running": process.name,
                "executions_left": process.total_executions - process.executions,
                "waiting_processes": get_processes_names(waiting_processes),
            }
        )
        self._update_process(time, process)
        self._sort_table()

    def _update_process(self, time: int, process: Process) -> None:
        if process.has_finished():
            process.finish_time = time

        for i, p in enumerate(self.processes):
            if process.name == p.name:
                self.processes[i] = process
                break
        else:
            self.processes.append(process)

    def _sort_table(self) -> None:
        self.executions = sorted(self.executions, key=lambda d: d["time"])

    def show_table(self) -> None:
        for execution in self.executions:
            time = execution["time"]
            process = execution["process_running"]
            executions_left = execution["executions_left"]
            waiting_processes = execution["waiting_processes"]
            print(
                f"time: {time} \tprocess: {process}\texecutions_left: {executions_left}\twaiting_processes: {waiting_processes}"
            )

    def get_execution_string(self) -> None:
        return "".join([e["process_running"] for e in self.executions])

    def get_first_execution_time(self, process_name: str) -> int:
        for execution in self.executions:
            if process_name in execution["process_running"]:
                return execution["time"]

    def __len__(self) -> int:
        return len(self.executions)


class InteractiveSystem:
    def get_wait_time(table: ExecutionsTable) -> list[tuple[str, int]]:
        processes_wait_time = [
            (p.name, table.get_first_execution_time(p.name) - p.arrival_time)
            for p in table.processes
        ]
        avarage = sum([wait_time[1] for wait_time in processes_wait_time]) / len(
            processes_wait_time
        )

        return [processes_wait_time, f"Avarage: {avarage}"]

    def round_robin(
        processes: list[InteractiveProcess], time_slice, with_modification: bool = False
    ) -> tuple[ExecutionsTable]:
        activated_processes = find_first_processes(processes)
        running_process = activated_processes[0]
        slept_processes = [p for p in processes if p not in activated_processes]
        table = ExecutionsTable()
        time = activated_processes[0].arrival_time

        while slept_processes or activated_processes:
            # Execute process
            running_process = activated_processes[0]
            running_process.execute()
            table.add_execution(time, running_process, activated_processes[1::])

            # Update activated_processes
            time += 1
            if running_process.has_finished():
                activated_processes.pop(0)
            elif running_process.consecutive_executions == time_slice:
                running_process.consecutive_executions = 0
                activated_processes = [*activated_processes[1::], running_process]

            # Check if a process activates
            new_processes, slept_processes = get_new_processes(time, slept_processes)
            activated_processes = [*activated_processes, *new_processes]

            if new_processes and with_modification:
                # In round robin with modification, the new process has
                # priority over the process that just finished running
                swap_processes(
                    activated_processes,
                    len(activated_processes) - 1,
                    len(activated_processes) - 2,
                )

        return table


class BatchSystem:
    def get_wait_time(table: ExecutionsTable) -> list[tuple[str, int]]:
        processes_wait_time = [
            (p.name, table.get_first_execution_time(p.name) - p.arrival_time)
            for p in table.processes
        ]
        avarage = sum([wait_time[1] for wait_time in processes_wait_time]) / len(
            processes_wait_time
        )

        return [processes_wait_time, f"Avarage: {avarage}"]

    def shortest_job_first(processes: list[Process]):
        first_processes = find_first_processes(processes)
        first_processes_sorted = sort_processes_by_total_executions(first_processes)
        running_process = first_processes_sorted[0]
        activated_processes = first_processes_sorted[1::]
        slept_processes = [p for p in processes if p not in first_processes]
        table = ExecutionsTable()
        time = running_process.arrival_time

        while slept_processes or running_process:
            # Execute process
            running_process.execute()
            table.add_execution(time, running_process, activated_processes)
            time += 1

            # Find new processes
            new_processes, slept_processes = get_new_processes(time, slept_processes)
            activated_processes = sort_processes_by_total_executions(
                [*activated_processes, *new_processes]
            )
            if running_process.has_finished():
                if activated_processes:
                    running_process = activated_processes[0]
                    activated_processes.pop(0)
                else:
                    running_process = None

        return table

    def first_come_first_served(processes: list[Process]):
        first_processes = find_first_processes(processes)
        running_process = first_processes[0]
        activated_processes = first_processes[1::]
        slept_processes = [p for p in processes if p not in first_processes]
        table = ExecutionsTable()
        time = running_process.arrival_time

        while activated_processes or running_process:
            running_process.execute()
            table.add_execution(time, running_process, activated_processes)
            time += 1

            activated_processes += get_new_processes(time, slept_processes)[0]

            if running_process.has_finished():
                if activated_processes:
                    running_process = activated_processes[0]
                    activated_processes.pop(0)
                else:
                    running_process = None

        return table

    def shortest_remaining_time_next(processes: list[Process]):
        first_processes = find_first_processes(processes)
        first_processes_sorted = sort_processes_by_total_executions(first_processes)
        running_process = first_processes_sorted[0]
        activated_processes = first_processes_sorted[1::]
        slept_processes = [p for p in processes if p not in first_processes]
        table = ExecutionsTable()
        time = running_process.arrival_time

        while slept_processes or running_process:
            # Execute process
            running_process.execute()
            table.add_execution(time, running_process, activated_processes)
            time += 1

            # Find new processes
            new_processes, slept_processes = get_new_processes(time, slept_processes)
            new_processes_sorted = sort_processes_by_total_executions(new_processes)

            # If a new process have less remaining executions than the running
            # process, start executing the new process:
            if new_processes:
                if (
                    new_processes_sorted[0].remaining_executions
                    < running_process.remaining_executions
                ):
                    activated_processes.insert(0, running_process)
                    running_process = new_processes_sorted[0]
                    new_processes_sorted.pop(0)

            # Update activated proccesses
            activated_processes = sort_processes_by_total_executions(
                [*activated_processes, *new_processes_sorted]
            )

            # Check if running process has finished
            if running_process.has_finished():
                if activated_processes:
                    running_process = activated_processes[0]
                    activated_processes.pop(0)
                else:
                    running_process = None

        return table
