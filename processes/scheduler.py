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
        return [
            (p.name, table.get_first_execution_time(p.name) - p.arrival_time)
            for p in table.processes
        ]

    def round_robin(
        processes: list[Process], with_modification: bool = False
    ) -> tuple[ExecutionsTable]:
        activated_processes = find_first_processes(processes)
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
            else:
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
