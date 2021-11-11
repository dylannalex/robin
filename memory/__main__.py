from memory import paging
from os import system


def wait(msg):
    print(msg)
    input("Press Enter to continue...")


def main():
    while True:

        print(
            """\t\tPaging Menu:\n
    [1] Get logical/virtual address length (in bits)
    [2] Get physical/real address length (in bits)
    """
        )
        opt = input("Enter an option: ")
        system("cls")
        if opt == "1":
            pages = int(input("Number of pages: "))
            page_size = int(input("Page space in bytes (i.e: 1024): "))
            wait(paging.get_logical_address_length(pages, page_size))

        if opt == "2":
            frames = int(input("Number of frames: "))
            frame_size = int(input("Frame space in bytes (i.e: 1024): "))
            wait(paging.get_physical_address_length(frames, frame_size))


if __name__ == "__main__":
    main()
