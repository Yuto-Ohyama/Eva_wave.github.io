#%%
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

hero_hp = 30
hero_attack = 5

slime = Monster("スライム", 10, 1)
drakey = Monster("ドラキー", 13, 2)
doragon = Monster("ドラゴン", 30, 5)
darkdream = Monster("ダークドレアム", 130000, 999)

import random
monsters = [slime, drakey, doragon, darkdream]
appeard_monster = random.choice(monsters)

print(appeard_monster.name + "が現れた！")
while hero_hp > 0:
    print("勇者の攻撃！")

    appeard_monster.hp -= hero_attack

    if appeard_monster.hp > 0:
        print(appeard_monster.name + "は" + str(hero_attack) + "のダメージを受けた！")
        print(" ")

    else:
        print(appeard_monster.name + "は" + str(hero_attack) + "のダメージを受けた！")
        print(appeard_monster.name + "は力尽きた")
        print(" ")
        print("勇者は戦闘に勝った！")
        break
    
    print(appeard_monster.name + "の攻撃！")
    print("勇者は" + str(appeard_monster.attack) + "のダメージを受けた！")
    print(" ")

    hero_hp -= appeard_monster.attack

else:
    print("勇者は力尽きた")
    print(" ")
    print("勇者は戦闘に負けた！")

#%% 
