from typing import Union
from os_utn.operating_system.processes import process
from os_utn.operating_system.processes import scheduler

from os import system


OPTIONS = """[0] Add processes string
[1] Add process
[2] Remove process
[3] Remove all processes
[4] Show processes
[5] Scheduler algorithms
[6] Exit
"""

ALGORITHMS = """Select one of the following algorithms:


[1] Round robin
[2] SJF (shortest job fist)
[3] FCFS (First come first served)
[4] SRTN (Shortest remaining time next)
[5] Back
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
            print("\t\tPROCESSES MENU\n")
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
        return process.Process(name, arrival_time, total_executions)


def remove_process(processes) -> list[process.Process]:
    process_name = input("Enter process name: ")
    if process_name in process.get_processes_names(processes):
        if confirm(f"Are you sure you want to delete {process_name}? (y/n): "):
            return [p for p in processes if p.name != process_name]
    return processes


def show_processes(processes: list[process.Process]) -> None:
    for p in processes:
        print(
            f"name: {p.name}\t\tarrival time: {p.arrival_time}\t\ttotal executions: {p.total_executions}"
        )


def reset_attributes(processes: list[process.Process]):
    for process in processes:
        process.reset()


def main():
    processes = []
    while True:
        opt = menu(OPTIONS)
        system("cls")
        if opt == 0:
            print("FORMAT: \t\tprocessName-arrivalTime-totalExecutions,*-*-*,...")
            print("EXAMPLE:\t\tA-1-5,B-2-6,C-3-8\n\n")
            processes_str = input("Enter processes: ")
            processes = process.ProcessList.parse_processes_string(processes_str)

        if opt == 6:
            return

        if opt == 1:
            process_ = get_process()
            if process_:
                processes.append(process_)

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
                reset_attributes(processes)
                opt = menu(ALGORITHMS)
                system("cls")
                if opt == 1:
                    time_slice = int(input("Enter time slice: "))
                    with_modification = (
                        True
                        if input("With modification? (y/n): ").strip().lower() == "y"
                        else False
                    )
                    with_modification_change_times = []
                    while True:
                        ask_new_with_modification = (
                            input("Add new 'with modification' change? (y/n): ")
                            .strip()
                            .lower()
                        )
                        if ask_new_with_modification == "y":
                            try:
                                with_modification_change_times.append(
                                    int(input("Add change time: "))
                                )
                            except Exception as e:
                                print(f"Oops, something went wrong: {e}")
                                stop()
                        if ask_new_with_modification == "n":
                            break

                    system("cls")
                    table = scheduler.InteractiveSystem.round_robin(
                        processes,
                        time_slice,
                        with_modification,
                        with_modification_change_times,
                    )
                    table.show_table()
                    print(f"\n\nExecution string: {table.get_execution_string()}")
                    print(
                        f"\nWait time: {scheduler.InteractiveSystem.get_wait_time(table)}\t(LAST METHOD EXPLAINED BY TEACHER)"
                    )
                    print(
                        f"Wait time: {scheduler.InteractiveSystem.get_wait_time2(table)}\t(METHOD USED IN EXAMS)"
                    )
                    print(
                        f"\n\nReturn time: {scheduler.InteractiveSystem.get_return_time(table)}"
                    )

                elif opt == 2:
                    table = scheduler.BatchSystem.shortest_job_first(processes)
                    table.show_table()
                    print(f"\n\nExecution string: {table.get_execution_string()}")
                    print(f"Wait time: {scheduler.BatchSystem.get_wait_time(table)}")

                elif opt == 3:
                    table = scheduler.BatchSystem.first_come_first_served(processes)
                    table.show_table()
                    print(f"\n\nExecution string: {table.get_execution_string()}")
                    print(f"Wait time: {scheduler.BatchSystem.get_wait_time(table)}")

                elif opt == 4:
                    table = scheduler.BatchSystem.shortest_remaining_time_next(
                        processes
                    )
                    table.show_table()
                    print(f"\n\nExecution string: {table.get_execution_string()}")
                    print(f"Wait time: {scheduler.BatchSystem.get_wait_time(table)}")

                elif opt == 5:
                    break

                stop()


if __name__ == "__main__":
    main()
