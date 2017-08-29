import time
def fight(hero_stats, enemy_stats):
    while enemy_stats["HP"] > 0 and hero_stats["HP"] > 0:
        damage = (hero_stats.get("attack")-enemy_stats.get("defense"))
        enemy_stats["HP"] -= damage
        print(enemy_stats)
        time.sleep(0.5)
        if enemy_stats["HP"] > 0:
            damage = (enemy_stats.get("attack")-hero_stats.get("defense"))
            hero_stats["HP"] -= damage
            print(hero_stats)
            time.sleep(0.5)


def main():
    hero_stats = {"name": "Ja", "HP": 100, "attack": 50, "defense": 30, "exp": 0, "position": [0,0]}
    enemy_stats = {"name": "Ork", "HP": 100, "attack": 60, "defense": 30, "exp": 20}
    fight(hero_stats, enemy_stats)

main()