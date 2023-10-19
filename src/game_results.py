import os
from map import Map


def lose():
    os.system('clear')
    print(r"     ____    _    __  __ _____ ", end="\n")
    print(r"    / ___|  / \  |  \/  | ____|", end='\n')
    print(r"   | | __  / _ \ | |\/| |  _|  ", end='\n')
    print(r"   | |_\ \/ ___ \| |  | | |___ ", end='\n')
    print(r"    \____/_/   \_\_|__|_|_____|", end='\n')
    print(r"     / _ \ \   / / ____|  _ \  ", end='\n')
    print(r"    | | | \ \ / /|  _| | |_) | ", end='\n')
    print(r"    | |_| |\ V / | |___|  _ <  ", end='\n')
    print(r"     \___/  \_/  |_____|_| \_| ", end='\n')


def win():
    os.system('clear')
    print(r"   __        ______ _    _     ", end='\n')
    print(r"   \ \      / /____| |  | |    ", end='\n')
    print(r"    \ \ /\ / /  _| | |  | |    ", end='\n')
    print(r"     \ V  V /| |___| |__| |__  ", end='\n')
    print(r"    __\_/\_/_|_____|____|____| ", end='\n')
    print(r"   |  _ \ / _ \| \ | | ____| | ", end='\n')
    print(r"   | | | | | | |  \| |  _| | | ", end='\n')
    print(r"   | |_| | |_| | |\  | |___|_| ", end='\n')
    print(r"   |____/ \___/|_| \_|_____(_) ", end='\n')
    print(r"                ◯             ", end='\n')
    print(r"                ┃              ", end='\n')
    print(r"             ╱☉▔☉▔☉╲           ", end='\n')
    print(r"           ▕╲▏┓---┏▕╱▏         ", end='\n')
    print(r"          ╭╮╲┉╰━━━╯┉╱╭╮        ", end='\n')
    print(r"         ╭┛┣━╲ --- ╱━┫┗╮       ", end='\n')
    print(r"         ╰━┻━╮▔▔▔▔▔╭━┻━╯       ", end='\n')


def game_result(map):
    if map.win_flag == 1:
        win()

    elif map.lose_flag == 1:
        lose()

    return map.win_flag == 1 or map.lose_flag == 1
