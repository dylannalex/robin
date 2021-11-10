def get_avarage_input_output_time(
    rpm, sector_size, transfer_velocity, avarage_positioned_time, overload_time
):
    """
    rpm: revolutions per minute
    sector_size: bytes
    transfer_velocity: bytes/ms
    avarage_positioned_time: ms
    overload_time: ms
    """
    rps = rpm / 60
    avarage_rotation_time = round((0.5 / rps) * 1000, 2)
    transfer_time = round(sector_size / transfer_velocity, 2)
    return f"{round(round(avarage_positioned_time, 2) + avarage_rotation_time + transfer_time + round(overload_time, 2), 2)} ms"


def main():
    from input_output.units_converter import convert_transfer_velocity

    rpm = 3600
    sector_size = 1024
    transfer_velocity = convert_transfer_velocity(10, "MB", "s")
    avarage_positioned_time = 12
    overload_time = 2
    avarage_input_output_time = get_avarage_input_output_time(
        rpm, sector_size, transfer_velocity, avarage_positioned_time, overload_time
    )
    print(avarage_input_output_time)


if __name__ == "__main__":
    main()
