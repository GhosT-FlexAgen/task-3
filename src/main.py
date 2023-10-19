import readchar
from enemy import Enemy
from hero import Hero
from map import Map, doRecursiveDivision
from game_results import game_result

def game():
    map = Map(21, 21, 1, 1)
    hero = Hero(map.start)
    doRecursiveDivision(map)
    enemy = Enemy(map, 5)
    map.showMap(hero, enemy)
    while True:
        c = str(readchar.readchar())
        if c == 'w':
            hero.move_W(map)
        elif c == 's':
            hero.move_S(map)
        elif c == 'a':
            hero.move_A(map)
        elif c == 'd':
            hero.move_D(map)
        else:
            break

        enemy.move_enemy(map)
        map.showMap(hero, enemy)

        if game_result(map):
            exit()

if __name__ == "__main__":
    game()
