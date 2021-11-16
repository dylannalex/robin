from processes.process import *


class ExecutionsTable:
    def __init__(self):
        self.processes = []
        self.executions = []

    def add_execution(self, time: int, process: Process, queue: list[Process]) -> None:
        self.executions.append(
            {
                "time": time,
                "process_running": process.name,
                "remaining_executions": process.remaining_executions,
                "queue": get_processes_names(queue),
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

    def show_table(self, show_remaining_executions=False) -> None:
        for execution in self.executions:
            time = execution["time"]
            process_running = execution["process_running"]
            remaining_executions = execution["remaining_executions"]
            queue = execution["queue"]

            if show_remaining_executions:
                execution_stats = [
                    f"time: {time} ",
                    f"running: {process_running}  ({remaining_executions} remaining executions)",
                    f"queue: {queue}",
                ]
            else:
                execution_stats = [
                    f"time: {time} ",
                    f"running: {process_running}",
                    f"queue: {queue}",
                ]

            print("\t".join(execution_stats))

    def get_execution_string(self) -> None:
        return "".join([e["process_running"] for e in self.executions])

    def get_first_execution_time(self, process_name: str) -> int:
        for execution in self.executions:
            if process_name in execution["process_running"]:
                return execution["time"]

    def get_last_execution_time(self, process_name: str) -> int:
        for execution in self.executions:
            if (
                process_name in execution["process_running"]
                and execution["remaining_executions"] == 0
            ):
                return execution["time"]

    def __len__(self) -> int:
        return len(self.executions)


class InteractiveSystem:
    def get_return_time(table: ExecutionsTable) -> list[tuple[str, int]]:
        processes_return_time = [
            (p.name, table.get_last_execution_time(p.name) - p.arrival_time + 1)
            for p in table.processes
        ]
        avarage = sum([wait_time[1] for wait_time in processes_return_time]) / len(
            processes_return_time
        )

        return [processes_return_time, f"Avarage: {avarage}"]

    def get_wait_time(table: ExecutionsTable) -> list[tuple[str, int]]:
        processes_wait_time = [
            (p.name, table.get_first_execution_time(p.name) - p.arrival_time)
            for p in table.processes
        ]
        avarage = sum([wait_time[1] for wait_time in processes_wait_time]) / len(
            processes_wait_time
        )

        return [processes_wait_time, f"Avarage: {avarage}"]

    def get_wait_time2(table: ExecutionsTable) -> list[tuple[str, int]]:
        wait_time = [
            (
                p.name,
                table.get_last_execution_time(p.name)
                - p.arrival_time
                + 1
                - p.total_executions,
            )
            for p in table.processes
        ]
        avarage = sum([wait_time[1] for wait_time in wait_time]) / len(wait_time)

        return [wait_time, f"Avarage: {avarage}"]

    def round_robin(
        processes: list[InteractiveProcess], time_slice, with_modification: bool = False
    ) -> tuple[ExecutionsTable]:
        queue = find_first_processes(processes)
        running_process = queue[0]
        slept_processes = [p for p in processes if p not in queue]
        table = ExecutionsTable()
        time = queue[0].arrival_time

        while slept_processes or queue:
            # Execute process
            running_process = queue[0]
            running_process.execute()
            table.add_execution(time, running_process, queue[1::])

            # Update queue
            time += 1
            if running_process.has_finished():
                queue.pop(0)
            elif running_process.consecutive_executions == time_slice:
                running_process.consecutive_executions = 0
                queue = [*queue[1::], running_process]

            # Check if a process activates
            new_processes, slept_processes = get_new_processes(time, slept_processes)
            queue = [*queue, *new_processes]

            if new_processes and with_modification:
                # In round robin with modification, the new process has
                # priority over the process that just finished running
                swap_processes(
                    queue,
                    len(queue) - 1,
                    len(queue) - 2,
                )

        return table


class BatchSystem:
    def get_wait_time(table: ExecutionsTable) -> list[tuple[str, int]]:
        processes_return_time = [
            (p.name, table.get_last_execution_time(p.name) - p.arrival_time + 1)
            for p in table.processes
        ]
        avarage = sum([wait_time[1] for wait_time in processes_return_time]) / len(
            processes_return_time
        )

        return [processes_return_time, f"Avarage: {avarage}"]

    def shortest_job_first(processes: list[Process]):
        first_processes = find_first_processes(processes)
        first_processes_sorted = sort_processes_by_total_executions(first_processes)
        running_process = first_processes_sorted[0]
        queue = first_processes_sorted[1::]
        slept_processes = [p for p in processes if p not in first_processes]
        table = ExecutionsTable()
        time = running_process.arrival_time

        while slept_processes or running_process:
            # Execute process
            running_process.execute()
            table.add_execution(time, running_process, queue)
            time += 1

            # Find new processes
            new_processes, slept_processes = get_new_processes(time, slept_processes)
            queue = sort_processes_by_total_executions([*queue, *new_processes])
            if running_process.has_finished():
                if queue:
                    running_process = queue[0]
                    queue.pop(0)
                else:
                    running_process = None

        return table

    def first_come_first_served(processes: list[Process]):
        first_processes = find_first_processes(processes)
        running_process = first_processes[0]
        queue = first_processes[1::]
        slept_processes = [p for p in processes if p not in first_processes]
        table = ExecutionsTable()
        time = running_process.arrival_time

        while queue or running_process:
            running_process.execute()
            table.add_execution(time, running_process, queue)
            time += 1

            queue += get_new_processes(time, slept_processes)[0]

            if running_process.has_finished():
                if queue:
                    running_process = queue[0]
                    queue.pop(0)
                else:
                    running_process = None

        return table

    def shortest_remaining_time_next(processes: list[Process]):
        first_processes = find_first_processes(processes)
        first_processes_sorted = sort_processes_by_total_executions(first_processes)
        running_process = first_processes_sorted[0]
        queue = first_processes_sorted[1::]
        slept_processes = [p for p in processes if p not in first_processes]
        table = ExecutionsTable()
        time = running_process.arrival_time

        while slept_processes or running_process:
            # Execute process
            running_process.execute()
            table.add_execution(time, running_process, queue)
            time += 1

            # Find new processes
            new_processes, slept_processes = get_new_processes(time, slept_processes)
            new_processes_sorted = sort_processes_by_total_executions(new_processes)

            # If a new process have less remaining current_executions than the running
            # process, start executing the new process:
            if new_processes:
                if (
                    new_processes_sorted[0].remaining_executions
                    < running_process.remaining_executions
                ):
                    queue.insert(0, running_process)
                    running_process = new_processes_sorted[0]
                    new_processes_sorted.pop(0)

            # Update activated proccesses
            queue = sort_processes_by_remaining_executions(
                [*queue, *new_processes_sorted]
            )
            # Check if running process has finished
            if running_process.has_finished():
                if queue:
                    running_process = queue[0]
                    queue.pop(0)
                else:
                    running_process = None

        return table
