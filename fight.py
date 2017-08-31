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
    print("\n\n")
    for key in data:
        if key not in data["except"]:
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
    hit_chance_hero = count_hit_chance(data.get("hero_dexterity")[0], data.get("enemy_dexterity")[0])

    while data["enemy_HP"][0] > 0 and data["hero_HP"][0] > 0:

        hit_check = random.randint(0, 100)
        if data["hero_HP"][0] > 0 and hit_check <= hit_chance_hero:
            damage = (data.get("hero_attack")[0]-data.get("enemy_defense")[0])
            if damage < 0:
                damage = 0
            data["enemy_HP"][0] -= damage
            if data["enemy_HP"][0] < 0:
                data["enemy_HP"][0] = 0
            data["hero_message"][0] = "You attacked for "+str(damage)+" damage."
        elif data["hero_HP"][0] > 0 and hit_check > hit_chance_hero:
            data["hero_message"][0] = "You missed"
        print_screen(background, data)
        time.sleep(1)
        data["hero_message"][0] = ""

        hit_check = random.randint(0, 100)
        if data["enemy_HP"][0] > 0 and hit_check <= hit_chance_enemy:
            damage = (data.get("enemy_attack")[0]-data.get("hero_defense")[0])
            if damage < 0:
                damage = 0   
            data["hero_HP"][0] -= damage
            if data["hero_HP"][0] < 0:
                data["hero_HP"][0] = 0
            data["enemy_message"][0] = data["enemy_name"][0] + " attacked you for "+str(damage)+" damage."
        elif data["enemy_HP"][0] > 0 and hit_check > hit_chance_enemy:
            data["enemy_message"][0] = data["enemy_name"][0] + " missed."
        print_screen(background, data)
        time.sleep(1)
        data["enemy_message"][0] = ""

        if data["hero_HP"][0] > 0 and data["enemy_HP"][0] <= 0:
            data["hero_exp"][0] += data["enemy_exp"][0]
            inv = data["inventory"]
            inv["gold coin"][1] += data["enemy_gold"][0]
            data["hero_message"][0] = "You gained " + str(data["enemy_gold"][0]) + " gold and " + str(data["enemy_exp"][0]) + " exp"
            print_screen(background, data)
            time.sleep(2)


def game_fight(data):
    background = load_level("battle_screen.txt")
    fight(data, background)
    return data


if __name__ == '__game_fight__':
    game_fight(data)
