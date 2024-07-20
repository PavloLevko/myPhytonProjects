import time
import os
wolf = '🐺'
sheep = '🐑'
wolf_pos = 0
sheep_pos = 3


fild_len = 20

def clear_console():
    # Встановлення змінної TERM для Unix-подібних систем
    if os.name != 'nt' and 'TERM' not in os.environ:
        os.environ['TERM'] = 'xterm-256color'

    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix-подібні системи (Linux, macOS)
    else:
        os.system('clear')

def create_fild(wolf_pos, sheep_pos, fild_len):
    fild = ['🍀'] * fild_len
    fild[sheep_pos] = sheep
    fild[wolf_pos] = wolf
    if wolf_pos == sheep_pos:
        print("Wolf eat sheep")
    return fild


while wolf_pos != sheep_pos:
    sheep_pos += 2
    if sheep_pos == fild_len-1:
        sheep_pos = 0
    time.sleep(1)
    wolf_pos += 1
    if wolf_pos == fild_len-1:
        wolf_pos = 0

    print(create_fild(wolf_pos, sheep_pos, fild_len))



