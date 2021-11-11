def fix_length(n: str, length: int):
    if len(n) > length:
        raise ValueError(f"n ({n}) cannot be greater than {length}")

    while len(n) < length:
        n = "0" + n

    return n


def show_character_on_screen(row, col, add_comments=True):
    if add_comments:
        return f"""
ORG 100h
MOV AH, 00H
INT 16H       \t; Keyboard service: reads only one character
MOV DH, {row} \t; row {row}
MOV DL, {col} \t; column {col}
MOV BH, 00    \t; page number 0
MOV AH, 02
INT 10H    \t; Video service
MOV DL, AL \t; Moves character to DL
INT 21H    \t; MSDOS service: prints character (stored in DL) on screen
RET"""

    return f"""
ORG 100H
MOV AH, 00H
INT 16H 
MOV DH, {row}
MOV DL, {col}
MOV BH, 00
INT 10H  
MOV DL, AL
INT 21H
RET"""


def show_string_on_screen_with_int21(string, row=0, col=0, add_comments=True):
    hex_row = fix_length(str(row), 2)
    hex_col = fix_length(str(col), 2)

    if add_comments:
        return f"""
ORG 100H
JMP MAIN
STRING DB "{string}$" \t; "$" indicates the end of the string
MAIN: 
      MOV DH, {hex_row} \t\t; row {row}
      MOV DL, {hex_col} \t\t; column {col}
      MOV BH, 00  \t\t; prints in first screen (screen 00)
      MOV AH, 02
      INT 10H
      MOV AH,09H
      MOV DX,OFFSET STRING
      INT 21H
      HLT                                   
      RET            
"""
    return f"""
ORG 100H
JMP MAIN
STRING DB "{string}$"
MAIN: 
      MOV DH, {hex_row}
      MOV DL, {hex_col}
      MOV BH, 00
      MOV AH, 02
      INT 10H  
      MOV AH,09H
      MOV DX,OFFSET STRING 
      INT 21H
      HLT                                   
      RET  
"""


def show_string_on_screen_with_int10(string, row=0, col=0, add_comments=True):
    hex_row = fix_length(str(row), 2)
    hex_col = fix_length(str(col), 2)
    hex_string_length = fix_length(str(hex(len(string))).split("x")[1].upper(), 2)

    if add_comments:
        return f"""
ORG 100H
JMP MAIN
MSG DB "{string}"
MAIN:
    LEA BP, MSG
    MOV AH, 13H \t; loads int 10 serviceses 
    MOV AL, 00  \t; reads hole string (doesn't move cursor)
    MOV DX, {hex_row}{hex_col}H \t; prints string starting on row {row} and column {col}
    MOV BH, 00 \t\t; prints string in first screen (screen 00)
    MOV BL, 1EH \t; yellow text and blue background
    MOV CX, {hex_string_length}H \t; string length is {len(string)} ({hex_string_length} in hexadecimal)
    INT 10H
    RET
"""

    return f"""
ORG 100H
JMP MAIN
MSG DB "{string}"
MAIN:
    LEA BP, MSG
    MOV AH, 13H
    MOV AL, 00
    MOV DX, {hex_row}{hex_col}H
    MOV BH, 00 \t\t; prints string in first screen (screen 00)
    MOV BL, 1EH \t; yellow text and blue background
    MOV CX, {hex_string_length}H
    INT 10H
    RET
"""
