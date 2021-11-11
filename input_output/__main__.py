from input_output import units_converter, hdd, assembly, uart
from os import system


def get_hdd_parameters():
    rpm = int(input("Enter rpm: "))

    sector_size = input("Enter sector size: ")
    sector_size_n, sector_size_unit = units_converter.decompose_number(sector_size)
    converted_sector_size = units_converter.convert_size_unit(
        sector_size_n, sector_size_unit
    )

    transfer_velocity = input("Enter transfer velocity: ")
    transfer_velocity_n, transfer_velocity_unit = units_converter.decompose_number(
        transfer_velocity
    )
    converted_transfer_velocity = units_converter.convert_transfer_velocity(
        transfer_velocity_n, *transfer_velocity_unit.split("/")
    )

    avarage_positioned_time = input("Enter avarage positioned time: ")
    (
        avarage_positioned_time_n,
        avarage_positioned_time_unit,
    ) = units_converter.decompose_number(avarage_positioned_time)
    converted_avarage_positioned_time = units_converter.convert_size_unit(
        avarage_positioned_time_n, avarage_positioned_time_unit
    )

    overload_time = input("Enter overload time: ")
    overload_time_n, overload_time_unit = units_converter.decompose_number(
        overload_time
    )
    converted_overload_time = units_converter.convert_size_unit(
        overload_time_n, overload_time_unit
    )

    return (
        rpm,
        converted_sector_size,
        converted_transfer_velocity,
        converted_avarage_positioned_time,
        converted_overload_time,
    )


def assembly_menu():
    print(
        """Select an option:
[1] Show character on screen
[2] Show string on screen with int21
[3] Show string on screen with int10
[4] Back
"""
    )
    opt = int(input("Enter an option: "))

    if opt not in (1, 2, 3):
        return

    system("cls")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    add_comments = (
        True if input("Show comments (y/n): ").strip().lower() == "y" else False
    )
    if opt == 1:
        result = assembly.show_character_on_screen(row, col, add_comments)
    else:
        string = input("Enter string: ")
        if opt == 2:
            result = assembly.show_string_on_screen_with_int21(
                string, row, col, add_comments
            )
        if opt == 3:
            result = assembly.show_string_on_screen_with_int10(
                string, row, col, add_comments
            )

    wait(result)


def uart_menu():
    dlab_input = input(
        "Enable DLL and DLM access (if speed performance is required, this is probably 'y')(y/n): "
    )
    if dlab_input.strip().lower() == "y":
        dlab = True
    else:
        dlab = False

    break_control = (
        True if input("Break control (y/n): ").strip().lower() == "y" else False
    )
    parity = input("Parity (odd/even/mark/space): ").strip().lower()
    stop_bits = int(input("Stop bits (1/2): ").strip())
    word_length = int(input("Word length (5/6/7/8): ").strip())
    wait(
        uart.get_line_control_register(
            dlab, break_control, parity, stop_bits, word_length
        )
    )


def wait(msg):
    print(msg)
    input("Press Enter to continue...")


def main():
    while True:
        try:
            system("cls")
            print(
                """\t\tMENU
[1] Get avarage input/output time
[2] Generate assembly code
[3] Get UART LCR register bits"""
            )
            opt = int(input("Enter option: "))
            system("cls")
            if opt == 1:
                wait(hdd.get_avarage_input_output_time(*get_hdd_parameters()))
            if opt == 2:
                assembly_menu()
            if opt == 3:
                uart_menu()
        except Exception as error:
            wait(f"\nError: {error}")


if __name__ == "__main__":
    main()
