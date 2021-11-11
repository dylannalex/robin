from math import log2


def get_logical_address_length(pages, page_size):
    return round(log2(pages) + log2(page_size))


def get_physical_address_length(frame, frame_size):
    return round(log2(frame) + log2(frame_size))
