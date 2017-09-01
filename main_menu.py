import os
import time
import game


def print_from_file(filename):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(filename, "r") as file:
        print_screen = file.readlines()
        for line in print_screen:
            print(line, end="")


def print_from_file_with_input(filename):
    if filename == "highscore1.txt":
        pass
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    with open(filename, "r") as file:
        print_screen = file.readlines()
        for line in print_screen:
            print(line, end="")
    input("Press enter to return")


def length_of_longest(inventory, counter):
    longest = "a"
    for it in inventory:
        if len(it) > len(longest):
            longest = it
    return len(longest)


def character_creation():
    print_from_file("char_creation.txt")
    with open('game.sav', 'r') as inf:
        data = eval(inf.read())
    attack = data["hero_attack"][0]
    defense = data["hero_defense"][0]
    dexterity = data["hero_dexterity"][0]
    remaining_points = data["remaining_points"][0]
    name = input("Please enter name of your character: ")
    while remaining_points > 0:
        print_from_file("char_creation.txt")
        print("""
    Name: {}

    Your statistics:
    Remaining points: {}
    1. Dexterity: {}
    2. Attack   : {}
    3. Defense  : {} \n\n""".format(name, remaining_points, dexterity, attack, defense))
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
    print_from_file("char_creation.txt")
    print("""
    Name: {}

    Your statistics:
    Remaining points: {}
    1. Dexterity {}:
    2. Attack {}:
    3. Defense: {}""".format(name, remaining_points, dexterity, attack, defense))
    data["hero_name"][0] = name
    data["hero_HP"][0] = 100
    data["hero_attack"][0] = attack
    data["hero_defense"][0] = defense
    data["hero_dexterity"][0] = dexterity
    data["remaining_points"][0] = remaining_points
    time.sleep(2)
    return data


def play():
    while True:
        user_play = input()
        try:
            user_play = int(user_play)
            if user_play == 1:
                data = character_creation()
                print_from_file_with_input("introduction.txt")
                data["starttime"] = time.time()
                game.game(data)
            elif user_play == 2:
                print_from_file("mainmenu_ascii.txt")
                return
            else:
                continue
        except ValueError:
            print_from_file("play.txt")


def main():
    print_from_file("mainmenu_ascii.txt")
    while True:
        try:
            user_input = int(input())
            if user_input == 1:
                print_from_file("play.txt")
                play()
            elif user_input == 2:
                print_from_file_with_input("highscore.txt")
                print_from_file("mainmenu_ascii.txt")
            elif user_input == 3:
                print_from_file_with_input("how_to_play.txt")
                print_from_file("mainmenu_ascii.txt")
            elif user_input == 4:
                print_from_file_with_input("about_us_ascii.txt")
                print_from_file("mainmenu_ascii.txt")
            elif user_input == 5:
                quit()
            else:
                continue
        except ValueError:
            print_from_file("mainmenu_ascii.txt")


if __name__ == "__main__":
    main()
