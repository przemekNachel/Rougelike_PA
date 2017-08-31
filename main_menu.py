import os
import time


def print_from_file(filename):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(filename, "r") as file:
        print_screen = file.readlines()
        for line in print_screen:
            print(line, end="")


def print_from_file_with_input(filename):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(filename, "r") as file:
        print_screen = file.readlines()
        for line in print_screen:
            print(line, end="")
    input("Press enter to return")


def character_creation():
    print_from_file("char_creation.txt")
    attack = 10
    defense = 10
    dexterity = 10
    remaining_points = 20
    name = input("Please enter name of your character: ")
    while remaining_points > 0:
        print_from_file("char_creation.txt")
        print("""
    Name: {}

    Your statistics:
    Remaining points: {}
    1. Dexterity {}:
    2. Attack {}:
    3. Defense: {} \n\n""".format(name, remaining_points, dexterity, attack, defense))
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
    time.sleep(1)


def play():
    while True:
        user_play = input()
        try:
            user_play = int(user_play)
            if user_play == 1:
                character_creation()
                print_from_file_with_input("introduction.txt")
                import game
            elif user_play == 2:
                pass
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
                print_from_file_with_input("Highscore.txt")
                print_from_file("mainmenu_ascii.txt")
            elif user_input == 3:
                print_from_file_with_input("How_to_play.txt")
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

main()
