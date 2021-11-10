def show_character_on_screen(row, col):
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
INT 21H    \t; MSDOS service: prints character (in DL) on screen
RET"""
