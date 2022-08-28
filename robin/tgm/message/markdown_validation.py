SPECIAL_MARKDOWN_CHARS = (
    "_",
    "*",
    "[",
    "]",
    "(",
    ")",
    "~",
    "`",
    ">",
    "#",
    "+",
    "-",
    "=",
    "|",
    "{",
    "}",
    ".",
    "!",
)


def get_valid_message(text):
    """
    Returns the text but with a backslash added behind all special characters
    """
    valid_text = ""
    for character in str(text):
        if character in SPECIAL_MARKDOWN_CHARS:
            valid_text += f"\\{character}"
        else:
            valid_text += character

    return valid_text
