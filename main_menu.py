import os


def print_mainmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("mainmenu_ascii.txt", "r") as menu:
        menu_title = menu.readlines()
        for line in menu_title:
            print(line, end="")


def print_how_to_play():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("How_to_play.txt", "r") as how_to_play:
        how_to_play_screen = how_to_play.readlines()
        for line in how_to_play_screen:
            print(line, end="")
    input("Press enter to return")
    return


def print_highscore():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("Highscore.txt", "r") as highscore:
        highscore_screen = highscore.readlines()
        for line in highscore_screen:
            print(line, end="")
    input("Press enter to return")
    return


def print_about_us():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("about_us_ascii.txt", "r") as about_us:
        about_us_screen = about_us.readlines()
        for line in about_us_screen:
            print(line, end="")
    input("Press enter to return")
    return


def main():
    print_mainmenu()
    while True:
        try:
            user_input = int(input())
        except:
            print_mainmenu()
        if user_input == 1:
            pass
        elif user_input == 2:
            print_highscore()
            print_mainmenu()
        elif user_input == 3:
            print_how_to_play()
            print_mainmenu()
        elif user_input == 4:
            print_about_us()
            print_mainmenu()
        elif user_input == 5:
            quit()
        else:
            continue
main()