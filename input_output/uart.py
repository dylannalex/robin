def get_line_control_register(
    dlab: bool, break_control: bool, parity: str, stop_bits: int, word_length: int
):
    lcr = "1" if dlab else "0"
    lcr += "1" if break_control else "0"

    if parity in ("no parity", "none", "no"):
        lcr += "000"
    elif parity == "odd":
        lcr += "001"
    elif parity == "even":
        lcr += "011"
    elif parity == "mark":
        lcr += "101"
    elif parity == "space":
        lcr += "111"
    else:
        raise ValueError("Invalid parity value")

    if stop_bits == 1:
        lcr += "0"
    elif stop_bits == 2:
        lcr += "1"
    else:
        raise ValueError("Invalid stop_bits value")

    if word_length == 5:
        lcr += "00"
    elif word_length == 6:
        lcr += "01"
    elif word_length == 7:
        lcr += "10"
    elif word_length == 8:
        lcr += "11"
    else:
        raise ValueError("Invalid word_length value")

    return lcr
