import os
import time


def load_level(file):
    map = []
    with open(file) as inputfile:
        for line in inputfile:
            map.append(line.strip())
    return map


def print_screen(map,data):
    covered_screen = list(map)
    print(chr(27) + "[2J")
    for key in data:
        covered_screen[data.get(key)[1]] = (covered_screen[data.get(key)[1]][:data.get(key)[2]] + 
                                           str(data.get(key)[0]) + 
                                           covered_screen[data.get(key)[1]][data.get(key)[2] + 
                                           len(str(data.get(key)[0])):])
    for line in covered_screen:
        print("".join(line))
    print("\n\n")


def fight(data, background):
    hit_chance_enemy = (data.get("enemy_dexterity")[0] + data.get("hero_dexterity")[0])
    hit_chance_enemy = data.get("enemy_dexterity")[0] * 100 / hit_chance_enemy
    print(hit_chance_enemy)
    hit_chance_hero = data.get("hero_dexterity")[0] + data.get("enemy_dexterity")[0]
    hit_chance_hero = data.get("hero_dexterity")[0] * 100 / hit_chance_hero
    print(hit_chance_hero)
    while data["enemy_HP"][0] > 0 and data["hero_HP"][0] > 0:
        damage = (data.get("hero_attack")[0]-data.get("enemy_defense")[0])
        data["enemy_HP"][0] -= damage
        data["hero_message"][0] = "You get"+str(damage)+"0 hits"
        print_screen(background,data)
        time.sleep(0.5)
        if data["enemy_HP"][0] > 0:
            damage = (data.get("enemy_attack")[0]-data.get("hero_defense")[0])
            data["hero_HP"][0] -= damage
            print_screen(background,data)
            time.sleep(0.5)


def main():
    background = load_level("battle_screen.txt")
    data = {
        "hero_name": ["Ja",3,18], 
        "hero_HP": [100,4,18], 
        "hero_attack": [50,5,18], 
        "hero_defense": [30,6,18], 
        "hero_dexterity": [15, 7, 18], 
        "hero_exp": [0,8,18], 
        "hero_message": ["",10,50], 
        "enemy_name": ["Ork",3,129], 
        "enemy_HP": [100,4,129], 
        "enemy_attack": [60,5,129], 
        "enemy_defense": [30,6,129], 
        "enemy_dexterity": [15, 7, 129],
        "enemy_exp": [20,8,129], 
        "enemy_message": ["",10,50], 
            }
    hero_position = [0,0]
    fight(data, background)


main()