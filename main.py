import time
import random

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def load_level(file):
    map = []
    with open(file) as inputfile:
        for line in inputfile:
            map.append(line.strip())
    return map

def print_map(map):
    for line in map:
        print ("".join(line))
    print("\n\n")


def insert_objects_to_map(hero_position, map):
    covered_map = list(map)
    covered_map[hero_position[1]] = (
        str(map[hero_position[1]][:hero_position[0]]) +
        "@" +
        str(map[hero_position[1]][hero_position[0] + 1:]))
    print(chr(27) + "[2J")
    for line in covered_map:
        print ("".join(line))
    print("\n\n")
    return covered_map

def print_guardian(map, guardian):
    i=2
    for line in range(0,len(guardians_data[guardian]) - 2):
        word = map[guardians_data[guardian][0]+line]
        index = guardians_data[guardian][1]
        word = word[:index] + guardians_data[guardian][i] + word[index + len(guardians_data[guardian][i]):]
        map[line + guardians_data[guardian][0]] = word
        i+=1 
    for line in map:
        print ("".join(line))

def walking_on_grass(grass_steps_to_meet, monster_level):
    grass_steps_to_meet[1] += 1
    if grass_steps_to_meet[1] == grass_steps_to_meet[0]:
        grass_steps_to_meet[0] = random.randint(5, 13)
        grass_steps_to_meet[1] = 0
        grass_steps_to_meet[2] = 1


def handle_with_objects(hero_position, space_to_move, covered_map, objects, map, grass_steps, stats):    
    object_at_left = covered_map[hero_position[1]][hero_position[0]-1]
    object_at_right = covered_map[hero_position[1]][hero_position[0]+1]
    object_at_top = covered_map[hero_position[1]-1][hero_position[0]]
    object_at_bottom = covered_map[hero_position[1]+1][hero_position[0]]
    object_under_hero = map[hero_position[1]][hero_position[0]]
    if object_at_left in objects["obstacles"]:
        space_to_move["left"] = 0
    if object_at_right in objects["obstacles"]:
        space_to_move["right"] = 0
    if object_at_top in objects["obstacles"]:
        space_to_move["up"] = 0
    if object_at_bottom in objects["obstacles"]:
        space_to_move["down"] = 0
    if object_under_hero == ".":
        walking_on_grass(grass_steps, stats["monster_level"])

def battle_with_mob(level, input):
    print(chr(27) + "[2J")
    print(level)
    time.sleep(1)
    print("bla")


    


def moving(pressed_key, position, space_to_move):
        if pressed_key[0] == "a" and space_to_move["left"]:
            position[0] -= 1            
        if pressed_key[0] == "d" and space_to_move["right"]:
            position[0] += 1
        if pressed_key[0] == "w" and space_to_move["up"]:
            position[1] -= 1
        if pressed_key[0] == "s" and space_to_move["down"]:
            position[1] += 1

def main():
    map = list(load_level('1lvl.txt'))
    guardians_data = [[29, 24, "`oo.'", "`-')  ,.", " ( `-'/^`", " -`_-)"], []]
    
    objects = {"obstacles":["#", "^", "░", "▒", "▓"]}
    stats = {"hp":100, "atk":20, "def":20, "monster_level":1}
    position = [12,36]
    grass_steps_to_meet = [random.randint(5,13), 0, 0]

    pressed_key = [""]


    while True:
        map_with_objects = insert_objects_to_map(position, map)
        print_map(map_with_objects)
        pressed_key[0] = getch()
        if pressed_key[0] == "q":
            break
        space_to_move = {"left":1, "right":1, "up":1, "down":1}
        handle_with_objects(position, space_to_move, map_with_objects, objects, map, grass_steps_to_meet, stats)
        if grass_steps_to_meet[2]:
            grass_steps_to_meet[2] = 0
            while True:
                pressed_key[0] = getch()
                battle_with_mob(stats, pressed_key[0])
                if pressed_key[0] == "q": 
                    break          
        moving(pressed_key, position, space_to_move)



main()





