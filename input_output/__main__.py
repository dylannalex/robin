from input_output import units_converter, hdd, assembly
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


def get_assembler_parameters():
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    return row, col


def wait(msg):
    print(msg)
    input("Press Enter to continue...")


def main():
    while True:
        try:
            system("cls")
            print("[1] Get avarage input/output time\n[2] Get assembler code\n\n")
            opt = int(input("Enter option: "))
            system("cls")
            if opt == 1:
                wait(hdd.get_avarage_input_output_time(*get_hdd_parameters()))
            if opt == 2:
                wait(assembly.show_character_on_screen(*get_assembler_parameters()))
        except Exception as error:
            wait(f"\nError: {error}")


if __name__ == "__main__":
    main()
