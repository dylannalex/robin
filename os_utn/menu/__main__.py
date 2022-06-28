from os import system
from os_utn.menu import io_menu
from os_utn.menu import memory_menu
from os_utn.menu import processes_menu


def is_int(input_: str):
    try:
        int(input_)
        return True
    except ValueError:
        return False


def call_function(option: int):
    match option:
        case 1:
            processes_menu.main()
        case 2:
            memory_menu.main()
        case 3:
            io_menu.main()
        case 4:
            exit()


def menu():
    while True:
        system("cls")
        print(
            f"""
.: Operating System Tools :.

[1] Processes functions
[2] Memory functions
[3] Input/Output functions
[4] Exit

"""
        )
        option_selected = input("Enter option: ")
        if is_int(option_selected):
            call_function(int(option_selected))


if __name__ == "__main__":
    menu()
