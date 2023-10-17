import sys
from io import StringIO

sys.path.insert(1, './src/')
import main


def test_print_lose():
    stdout_lose = \
'     ____    _    __  __ _____ \n\
    / ___|  / \\  |  \\/  | ____|\n\
   | | __  / _ \\ | |\\/| |  _|  \n\
   | |_\\ \\/ ___ \\| |  | | |___ \n\
    \\____/_/   \\_\\_|__|_|_____|\n\
     / _ \\ \\   / / ____|  _ \\  \n\
    | | | \\ \\ / /|  _| | |_) | \n\
    | |_| |\\ V / | |___|  _ <  \n\
     \\___/  \\_/  |_____|_| \\_| \n'

    old_out = sys.stdout
    buff_io = StringIO()
    sys.stdout = buff_io
    main.lose()
    assert(buff_io.getvalue() == stdout_lose)
    sys.stdout = old_out


def test_print_win():
    stdout_win = \
'   __        ______ _    _     \n\
   \\ \\      / /____| |  | |    \n\
    \\ \\ /\\ / /  _| | |  | |    \n\
     \\ V  V /| |___| |__| |__  \n\
    __\\_/\\_/_|_____|____|____| \n\
   |  _ \\ / _ \\| \\ | | ____| | \n\
   | | | | | | |  \\| |  _| | | \n\
   | |_| | |_| | |\\  | |___|_| \n\
   |____/ \\___/|_| \\_|_____(_) \n\
                ◯             \n\
                ┃              \n\
             ╱☉▔☉▔☉╲           \n\
           ▕╲▏┓---┏▕╱▏         \n\
          ╭╮╲┉╰━━━╯┉╱╭╮        \n\
         ╭┛┣━╲ --- ╱━┫┗╮       \n\
         ╰━┻━╮▔▔▔▔▔╭━┻━╯       \n'

    old_out = sys.stdout
    buff_io = StringIO()
    sys.stdout = buff_io
    main.win()
    assert(buff_io.getvalue() == stdout_win)
    sys.stdout = old_out


def test_create_map():
    labyrint = main.Map(3, 3, 1, 1)
    main.doRecursiveDivision(labyrint)
    assert(labyrint.map == [[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert(labyrint.start == (1, 1))
    assert(labyrint.finish == (1, 1))
    assert(labyrint.lose_flag == 0)
    assert(labyrint.win_flag == 0)
    assert(labyrint.width == labyrint.height == 3)


def test_create_hero():
    labyrint = main.Map(3, 3, 1, 1)
    hero = main.Hero(labyrint.start)
    assert(hero.X == labyrint.start[0] == 1)
    assert(hero.Y == labyrint.start[1] == 1)


def test_create_enemy():
    labyrint = main.Map(5, 5, 1, 1)
    main.doRecursiveDivision(labyrint)
    enemy = main.Enemy(labyrint, 1)
    assert(enemy.enemy != [None, None])
    assert(labyrint.map[enemy.enemy[0][1]][enemy.enemy[0][0]] == 0)


def test_show_map():
    test_maze = \
'# # # # # \n\
# X     # \n\
# # # O # \n\
#     F # \n\
# # # # # \n'

    labyrint = main.Map(5, 5, 1, 1)
    hero = main.Hero(labyrint.start)
    main.doRecursiveDivision(labyrint)
    enemy = main.Enemy(labyrint, 1)
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    enemy.enemy = [(3, 2)]
    old_out = sys.stdout
    buff_io = StringIO()
    sys.stdout = buff_io
    labyrint.showMap(hero, enemy)
    assert(buff_io.getvalue() == test_maze)
    sys.stdout = old_out


def test_move_hero_positive():
    labyrint = main.Map(5, 5, 1, 1)
    hero = main.Hero(labyrint.start)
    main.doRecursiveDivision(labyrint)
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    hero.move_D(labyrint)
    # Смещение игрока вправо
    assert(hero.X == 1)
    assert(hero.Y == 2)
    hero.move_D(labyrint)
    hero.move_S(labyrint)
    # Смещение игрока вниз
    assert(hero.X == 2)
    assert(hero.Y == 3)
    hero.move_W(labyrint)
    # Смещение игрока вверх
    assert(hero.X == 1)
    assert(hero.Y == 3)
    hero.move_A(labyrint)
    # Смещение игрока влево
    assert(hero.X == 1)
    assert(hero.Y == 2)


def test_move_hero_negative():
    labyrint = main.Map(3, 3, 1, 1)
    hero = main.Hero(labyrint.start)
    main.doRecursiveDivision(labyrint)
    hero.move_W(labyrint)
    assert(hero.X == hero.Y == 1)
    hero.move_D(labyrint)
    assert(hero.X == hero.Y == 1)
    hero.move_S(labyrint)
    assert(hero.X == hero.Y == 1)
    hero.move_A(labyrint)
    assert(hero.X == hero.Y == 1)


def test_move_enemy_positive():
    # Test creating on this maze:
    # # # # #
    # X     #
    # # #   #
    # O   F #
    # # # # #
    labyrint = main.Map(5, 5, 1, 1)
    hero = main.Hero(labyrint.start)
    main.doRecursiveDivision(labyrint)
    enemy = main.Enemy(labyrint, 1)
    # Test move_D
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    enemy.enemy = [(1, 3)]
    enemy.move_enemy(labyrint)
    assert(enemy.enemy == [(2, 3)])
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
    enemy.move_enemy(labyrint)
    assert(enemy.enemy == [(3, 3)])
    # Test move_W
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1]]
    enemy.move_enemy(labyrint)
    assert(enemy.enemy == [(3, 2)])
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    enemy.move_enemy(labyrint)
    assert(enemy.enemy == [(3, 1)])
    # Test move_S
    enemy.move_enemy(labyrint)
    assert(enemy.enemy == [(3, 2)])
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    enemy.move_enemy(labyrint)
    # Test move_A
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    enemy.move_enemy(labyrint)
    assert(enemy.enemy == [(2, 1)])


def test_move_enemy_negative():
    labyrint = main.Map(3, 3, 1, 1)
    main.doRecursiveDivision(labyrint)
    labyrint.height = labyrint.width = 5
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    enemy = main.Enemy(labyrint, 1)
    enemy.enemy = [(1, 1)]
    labyrint.map = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    for i in range(100):
        enemy.move_enemy(labyrint)
        assert(enemy.enemy == [(1, 1)])


def test_game_win():
    test_maze = \
'# # # # \n\
# X F # \n\
# # # # \n'
    labyrint = main.Map(4, 3, 1, 1)
    main.doRecursiveDivision(labyrint)
    assert(labyrint.win_flag == labyrint.lose_flag == 0)

    hero = main.Hero(labyrint.start)
    enemy = main.Enemy(labyrint, 0)

    old_out = sys.stdout
    buff_io = StringIO()
    sys.stdout = buff_io
    labyrint.showMap(hero, enemy)
    assert(buff_io.getvalue() == test_maze)
    sys.stdout = old_out

    hero.move_D(labyrint)
    labyrint.showMap(hero, enemy)
    assert(labyrint.win_flag == 1)
    assert(labyrint.lose_flag == 0)


def test_game_lose():
    labyrint = main.Map(5, 5, 1, 1)
    main.doRecursiveDivision(labyrint)
    assert(labyrint.win_flag == labyrint.lose_flag == 0)

    hero = main.Hero(labyrint.start)
    enemy = main.Enemy(labyrint, 1)
    labyrint.map = [[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    enemy.enemy = [(2, 1)]

    hero.move_D(labyrint)
    labyrint.showMap(hero, enemy)
    assert(labyrint.win_flag == 0)
    assert(labyrint.lose_flag == 1)
