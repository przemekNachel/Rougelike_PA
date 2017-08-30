import os
import time
import random


def load_level(file):
    map = []
    with open(file) as inputfile:
        for line in inputfile:
            map.append(line.strip())
    return map


def print_screen(map):
    for line in map:
        print("".join(line))
    print("\n\n")


def fight(hero_stats, enemy_stats):
    hit_chance_enemy = (enemy_stats.get("dexterity") + hero_stats.get("dexterity"))
    hit_chance_enemy = enemy_stats.get("dexterity") * 100 / hit_chance_enemy
    print(hit_chance_enemy)
    hit_chance_hero = hero_stats.get("dexterity") + enemy_stats.get("dexterity")
    hit_chance_hero = hero_stats.get("dexterity") * 100 / hit_chance_hero
    print(hit_chance_hero)
    while enemy_stats["HP"] > 0 and hero_stats["HP"] > 0:
        random_chance_check = random.randint(1, 101)
        if random_chance_check <= hit_chance_hero:
            damage = (hero_stats.get("attack")-enemy_stats.get("defense"))
            enemy_stats["HP"] -= damage
            print("You attacked Ork for", damage, "your hp", hero_stats["HP"] )
            time.sleep(0.5)
        else: 
            print("You missed")
        random_chance_check = random.randint(1, 101)
        if enemy_stats["HP"] > 0 and random_chance_check <= hit_chance_enemy:
            damage = (enemy_stats.get("attack")-hero_stats.get("defense"))
            hero_stats["HP"] -= damage
            print("Ork attacked you for", damage, "he has hp", enemy_stats["HP"])
            time.sleep(0.5)
        else: 
            print("enemy missed you!")


def main():
    background = load_level("battle_screen.txt")
    print_screen(background)
    hero_stats = {"name": "Ja", "HP": 100, "attack": 50, "defense": 30, "dexterity" :20, "exp": 0, "position": [0,0]}
    enemy_stats = {"name": "Ork", "HP": 100, "attack": 60, "defense": 30, "dexterity": 40, "exp": 20}
    fight(hero_stats, enemy_stats)
    stats_hero = hero_stats.keys()
    print(hero_stats)

main()