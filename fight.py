import os
import time
import random


def load_level(file):
    map = []
    with open(file) as inputfile:
        for line in inputfile:
            map.append(line.strip())
    return map


def print_screen(map, data):
    covered_screen = list(map)
    os.system('cls' if os.name == 'nt' else 'clear')
    for key in data:
        if key != "enemy_exp":
            covered_screen[data.get(key)[1]] = (covered_screen[data.get(key)[1]][:data.get(key)[2]] +
                                                str(data.get(key)[0]) +
                                                covered_screen[data.get(key)[1]][data.get(key)[2] +
                                                len(str(data.get(key)[0])):])
    for line in covered_screen:
        print("".join(line))
    print("\n\n")


def count_hit_chance(attacker_dex, defender_dex):
    hit_chance = attacker_dex + defender_dex
    hit_chance = attacker_dex * 100 / hit_chance
    return hit_chance


def fight(data, background):

    hit_chance_enemy = count_hit_chance(data.get("enemy_dexterity")[0], data.get("hero_dexterity")[0])
    print(hit_chance_enemy)
    hit_chance_hero = count_hit_chance(data.get("hero_dexterity")[0], data.get("enemy_dexterity")[0])
    print(hit_chance_hero)

    while data["enemy_HP"][0] > 0 and data["hero_HP"][0] > 0:

        hit_check = random.randint(0, 100)
        if hit_check <= hit_chance_hero:
            damage = (data.get("hero_attack")[0]-data.get("enemy_defense")[0])
            data["enemy_HP"][0] -= damage
            data["hero_message"][0] = "You attacked for "+str(damage)+" damage."
            print_screen(background, data)
            time.sleep(0.5)
        else:
            data["hero_message"][0] = "You missed"

        hit_check = random.randint(0, 100)
        if data["enemy_HP"][0] > 0 and hit_check <= hit_chance_enemy:
            damage = (data.get("enemy_attack")[0]-data.get("hero_defense")[0])
            data["hero_HP"][0] -= damage
            data["enemy_message"][0] = data["enemy_name"][0] + " attacked you for "+str(damage)+" damage."
            print_screen(background, data)
            time.sleep(0.5)
        else:
            data["enemy_message"][0] = data["enemy_name"][0] + " missed."


def main():

    background = load_level("battle_screen.txt")
    data = {
        "hero_name": ["Ja", 3, 18],
        "hero_HP": [100, 4, 18],
        "hero_attack": [50, 5, 18],
        "hero_defense": [30, 6, 18],
        "hero_dexterity": [15, 7, 18],
        "hero_exp": [0, 8, 18],
        "hero_message": ["", 10, 50],
        "enemy_name": ["Ork", 3, 129],
        "enemy_HP": [100, 4, 129],
        "enemy_attack": [60, 5, 129],
        "enemy_defense": [30, 6, 129],
        "enemy_dexterity": [15, 7, 129],
        "enemy_exp": [20, 8, 129],
        "enemy_message": ["", 10, 50],
        }
    hero_position = [0, 0]
    fight(data, background)


main()
