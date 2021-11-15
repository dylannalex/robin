from typing import Union
from processes import process
from processes import scheduler
from os import system


OPTIONS = """Select one of the following options:

[0] Add processes string
[1] Add process
[2] Remove process
[3] Remove all processes
[4] Show processes
[5] Scheduler algorithms
"""

ALGORITHMS = """Select one of the following algorithms:


[1] Round robin
[2] SJF (shortest job fist)
[3] Back
"""


def stop() -> None:
    input("Press Enter to continue...")


def confirm(msg: str = "Are you sure? (y/n): ") -> bool:
    if input(msg).strip().lower() in ("y", "yes"):
        return True
    return False


def menu(options: str) -> int:
    warning = "\n\n"
    while True:
        try:
            system("cls")
            print(options)
            print(warning)
            return int(input("Enter option: "))

        except ValueError:
            warning = f"\nInvalid option\n"


def get_process() -> Union[None, process.Process]:
    name = input("Process name: ").strip()
    try:
        arrival_time = int(input("Arrival time: ").strip())
        total_executions = int(input("Executions: ").strip())
    except ValueError:
        return None

    if confirm():
        return process.InteractiveProcess(name, arrival_time, total_executions)


def parse_processes(processes_string: str) -> list[process.InteractiveProcess]:
    """
    Parses the given processes string.


    @processes_string: process_name-arrival_time-total_executions|process_name-arrival_time-total_executions...
    Example:
        A-1-5|B-2-6|C-3-8
        >>> [process.Process("A", 1, 5), process.Process("B", 2, 6), process.Process("C", 3, 8)]
    """
    processes_list = [l.split("-") for l in processes_string.split("|")]
    return [
        process.InteractiveProcess(p[0], int(p[1]), int(p[2])) for p in processes_list
    ]


def remove_process(processes) -> list[process.Process]:
    process_name = input("Enter process name: ")
    if processes in process.get_processes_names(processes):
        if confirm(f"Are you sure you want to delete {process_name}? (y/n): "):
            return [p for p in processes if p.name != process_name]


def show_processes(processes: list[process.Process]) -> None:
    for p in processes:
        print(
            f"name: {p.name}\t\tarrival time: {p.arrival_time}\t\ttotal executions: {p.total_executions}"
        )


def main():
    processes = []
    while True:
        opt = menu(OPTIONS)
        system("cls")
        if opt == 0:
            print(
                "FORMAT: \t\tprocess_name-arrival_time-total_executions|process_name-arrival_time-total_executions|..."
            )
            print("EXAMPLE:\t\tA-1-5|B-2-6|C-3-8\n\n")
            processes_str = input("Enter processes: ")
            processes = parse_processes(processes_str)

        if opt == 1:
            process = get_process()
            if process:
                processes.append(process)

        if opt == 2:
            processes = remove_process(processes)

        if opt == 3:
            if confirm("Are you sure you want to delete all processes? (y/n): "):
                processes = []

        if opt == 4:
            show_processes(processes)
            stop()

        if opt == 5:
            while True:
                opt = menu(ALGORITHMS)
                system("cls")
                if opt == 1:
                    time_slice = int(input("Enter time slice: "))
                    with_modification = (
                        True
                        if input("With modification? (y/n): ").strip() == "y"
                        else False
                    )
                    system("cls")
                    table = scheduler.InteractiveSystem.round_robin(
                        processes, time_slice, with_modification
                    )
                    table.show_table()
                    print(f"\n\nExecution string: {table.get_execution_string()}")
                    print(
                        f"Wait time: {scheduler.InteractiveSystem.get_wait_time(table)}"
                    )
                    stop()

                if opt == 2:
                    table = scheduler.BatchSystem.shortest_job_first(processes)
                    table.show_table()
                    print(f"\n\nExecution string: {table.get_execution_string()}")
                    print(f"Wait time: {scheduler.BatchSystem.get_wait_time(table)}")
                    stop()

                if opt == 3:
                    break


if __name__ == "__main__":
    main()
