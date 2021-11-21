from math import log2


def get_logical_address_length(pages, page_size):
    return round(log2(pages) + log2(page_size))


def get_physical_address_length(frame, frame_size):
    return round(log2(frame) + log2(frame_size))


def add_ceros(x: str, bits: int):
    return "".join(["0" for _ in range(bits)]) + x


def get_real_address(
    virtual_address: str,
    page_size: int,
    real_direction_bits: int = None,
):
    """
    virtual_address: bits (virtual address in binary)
    page_size: bytes
    real_direction_bits: int (number of bits)
    """
    if not real_direction_bits:
        real_direction_bits = len(virtual_address)
    displacement_bits = int(log2(page_size))
    displacement = f"0b{virtual_address[len(virtual_address) - displacement_bits ::]}"
    page = eval(f"0b{virtual_address[: len(virtual_address) - displacement_bits]}")
    page_frame = bin(int(input(f"Page number is {page}. Enter page frame: ")))
    real_direction = bin(eval(page_frame) * page_size + eval(displacement))[2::]
    return add_ceros(real_direction, real_direction_bits - len(real_direction))
