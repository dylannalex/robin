def convert_size_unit_to_bytes(n, size_unit):
    """
    Converts given size unit to bytes
    """
    scale_factor = 1

    if size_unit == "GB":
        scale_factor = 1024 ** 3

    elif size_unit == "MB":
        scale_factor = 1024 ** 2

    elif size_unit == "KB":
        scale_factor = 1024

    elif size_unit == "b":
        scale_factor = 1 / 8

    return n * scale_factor


def decompose_number(n):
    number = "".join([d for d in str(n) if d.isdigit()]).strip()
    unit = "".join([u for u in str(n) if u not in number]).strip()
    if not unit:
        unit = "B"
    return int(number), unit
