import os
import time
import random
import fight
import guardian


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


def print_map(map, data):
    covered_map = list(map)
    if data["guardians"][0]:
        i = 2
        for line in range(0, len(data["guardians"][data["current_location"]]) - 2):
            word = str(map[data["guardians"][data["current_location"]][0]+line])
            index = data["guardians"][data["current_location"]][1]
            word = word[:index] + str(data["guardians"][data["current_location"]][i]) + word[index + len(data["guardians"][data["current_location"]][i]):]
            covered_map[line + data["guardians"][data["current_location"]][0]] = word
            i + =1
    covered_map[data["hero_position"][1]] = (
        str(covered_map[data["hero_position"][1]][:data["hero_position"][0]]) +
        "@" +
        str(covered_map[data["hero_position"][1]][data["hero_position"][0] + 1:]))

    os.system('cls' if os.name == 'nt' else 'clear')
    for line in covered_map:
        print("".join(line))
    print("\n\n")
    return covered_map


def movement(pressed_key, data, map, covered_map):
    object_at_left = covered_map[data["hero_position"][1]][data["hero_position"][0]-1]
    object_at_right = covered_map[data["hero_position"][1]][data["hero_position"][0]+1]
    object_at_top = covered_map[data["hero_position"][1]-1][data["hero_position"][0]]
    object_at_bottom = covered_map[data["hero_position"][1]+1][data["hero_position"][0]]
    object_under_hero = map[data["hero_position"][1]][data["hero_position"][0]]
    obstacles = ["#", "^", "░", "▒", "▓"]
#  if object_at_top in data["guardians"][data["current_location"]][-1]:
    if object_at_top == "_":
        return 1
    if pressed_key == "a" and object_at_left not in obstacles:
        data["hero_position"][0] -= 1
    if pressed_key == "d" and object_at_right not in obstacles:
        data["hero_position"][0] += 1
    if pressed_key == "w" and object_at_top not in obstacles:
        data["hero_position"][1] -= 1
    if pressed_key == "s" and object_at_bottom not in obstacles:
        data["hero_position"][1] += 1
    if object_under_hero == ",":
        if data["grass_steps_remaining"][0]:
            data["grass_steps_remaining"][0] -= 1
        else:
            data["grass_steps_remaining"][0] = random.randint(5, 15)
            data["grass_steps_remaining"][1] = 1


def game():
    with open('game.sav', 'r') as inf:
        data = eval(inf.read())
    map = load_level(data["levels"][data["current_location"]])
    while True:
        covered_map = print_map(map, data)
        pressed_key = getch()
        guardian_over = movement(pressed_key, data, map, covered_map)
        if guardian_over:
            print("JUZ")
            data["guardians"][0] = 0
            guardian.fight_with_guardian([data["current_location"]])
        if pressed_key == "q":
            break
        if data["grass_steps_remaining"][1]:
            data["grass_steps_remaining"][1] = 0
            fight.game_fight()
          
 
game()
