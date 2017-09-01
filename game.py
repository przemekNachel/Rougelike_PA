import os
import time
import random
import fight
import guardian
import inventory
import main_menu


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
            i += 1
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
    obstacles = ["#", "^", "░", "▒", "▓"]
    if data["hero_HP"][0] < 100:
        data["hero_HP"][0] += 1
    if object_at_top in data["guardians"][data["current_location"]][-1]:
        return 1
    if pressed_key == "a" and object_at_left not in obstacles:
        data["hero_position"][0] -= 1
    if pressed_key == "d" and object_at_right not in obstacles:
        data["hero_position"][0] += 1
    if pressed_key == "w" and object_at_top not in obstacles:
        data["hero_position"][1] -= 1
    if pressed_key == "s" and object_at_bottom not in obstacles:
        data["hero_position"][1] += 1
    object_under_hero = map[data["hero_position"][1]][data["hero_position"][0]]
    if object_under_hero == ",":
        if data["grass_steps_remaining"][0]:
            data["grass_steps_remaining"][0] -= 1
        else:
            data["grass_steps_remaining"][0] = random.randint(5, 15)
            data["grass_steps_remaining"][1] = 1


def print_from_file(filename):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(filename, "r") as file:
        print_screen = file.readlines()
        for line in print_screen:
            print(line, end="")


def check_hero_level(data):
    if data["hero_exp"][0] >= (data["hero_level"][0] * 100):
        data["hero_exp"][0] -= (data["hero_level"][0] * 100)
        data["hero_level"][0] += 1
        data["lvlmessage"] = 1
        data["remaining_points"][0] += 10
    else:
        pass
    return data


def character_sheet(data):
    print_from_file("character_screen.txt")
    attack = data["hero_attack"][0]
    defense = data["hero_defense"][0]
    dexterity = data["hero_dexterity"][0]
    remaining_points = data["remaining_points"][0]
    name = data["hero_name"][0]
    exp = data["hero_exp"][0]
    lvl = data["hero_level"][0]
    hp = data["hero_HP"][0]
    remaining_exp = (lvl * 100) - exp
    while remaining_points > 0:
        print_from_file("character_screen.txt")
        print("""
    Name: {}

    Your statistics:
    Level: {}
    HP   : {}
    Exp  : {}
    Expierence to next level: {}

    Remaining points: {}
    1. Dexterity: {}
    2. Attack   : {}
    3. Defense  : {} \n\n""".format(name, lvl, hp, exp, remaining_exp, remaining_points, dexterity, attack, defense))
        answer = input("Please enter number from one to three to change stat by five points: ")
        if answer == "1":
            dexterity += 5
            remaining_points -= 5
        elif answer == "2":
            attack += 5
            remaining_points -= 5
        elif answer == "3":
            defense += 5
            remaining_points -= 5
        else:
            continue

    print_from_file("character_screen.txt")
    print("""
    Name: {}

    Your statistics:
    Level: {}
    HP   : {}
    Exp  : {}
    Expierence to next level: {}

    Remaining points: {}
    1. Dexterity: {}
    2. Attack   : {}
    3. Defense  : {} \n\n""".format(name, lvl, hp, exp, remaining_exp, remaining_points, dexterity, attack, defense))

    data["hero_name"][0] = name
    data["hero_HP"][0] = 100
    data["hero_attack"][0] = attack
    data["hero_defense"][0] = defense
    data["hero_dexterity"][0] = dexterity
    data["remaining_points"][0] = remaining_points
    return data


def check_enemy(data):
    enemieslvl1 = data["enemies1"]
    enemieslvl2 = data["enemies2"]
    if data["current_location"] == 1:
        current_enemy = random.choice(enemieslvl1)
    else:
        current_enemy = random.choice(enemieslvl2)
    print(current_enemy)
    data["enemy_name"][0] = current_enemy[0]
    data["enemy_HP"][0] = current_enemy[1]
    data["enemy_attack"][0] = current_enemy[2]
    data["enemy_defense"][0] = current_enemy[3]
    data["enemy_dexterity"][0] = current_enemy[4]
    data["enemy_exp"][0] = current_enemy[5]
    data["enemy_gold"][0] = current_enemy[6]


def check_if_alive(data):
    if data["hero_HP"][0] <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        with open("loose.txt", "r") as file:
            print_screen = file.readlines()
            for line in print_screen:
                print(line, end="")
        print("Monster killed you!")
        inv = data["inventory"]
        score = data["hero_level"][0] * inv["gold coin"][1]
        print("You gained", score, "points")
        hisghscore = [data["hero_name"][0], score]
        try:
            with open('highscore1', 'a') as export:
                for i in hisghscore:
                    i = str(i)
                    i += "\t"
                    export.writelines(i)
        except FileNotFoundError:
            print("uuu nie zapisze nie ma pliku!")
        input("Press enter to return")
        main_menu.main()


def game(data):
    map = load_level(data["levels"][data["current_location"]])
    while True:
        covered_map = print_map(map, data)
        if data["lvlmessage"] == 1:
            print("You gained level. Press 'C' to upgrade statistics.")
        pressed_key = getch()
        guardian_over = movement(pressed_key, data, map, covered_map)
        if guardian_over:
            guardian_over = 0
            data["guardians"][0] = 0
            guardian.fight_with_guardian(data)
        if pressed_key == "q":
            main_menu.main()
        if pressed_key == "i":
            inventory.inventory(data)
            pressed_key = getch()
        if pressed_key == "c":
            if data["lvlmessage"] == 1:
                data["lvlmessage"] = 0
            character_sheet(data)
            pressed_key = getch()
        print(data["hero_position"])
        if (data["hero_position"] == [34, 14] or data["hero_position"] == [33, 15]) and data["current_location"] == 1:
            data["current_location"] += 1
            data["guardians"][0] = 1
            game(data)
        if data["grass_steps_remaining"][1]:
            data["grass_steps_remaining"][1] = 0
            check_enemy(data)
            fight.game_fight(data)
            check_if_alive(data)
            check_hero_level(data)
