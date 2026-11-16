#%%
class Monster:
    def __init__(self, name, hp, mp, attack, defense, exp, gold):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.gold = gold
        
class Hero:
    def __init__(self, name, hp, mp, attack, defense, exp=0, level=1, gold=50):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.level = level
        self.gold = gold

    def gain_exp(self, amount):
        self.exp += amount
        self.gold += amount
        print(str(self.name) + "は" + str(amount) + "の経験値を獲得した！\n" + str(amount) + "ゴールドを手に入れた！")
        if self.exp >= 100: # 100経験値でレベルアップ
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 20  # レベルアップでHP増加
        self.mp += 5   # レベルアップでMP増加
        self.attack += 5  # レベルアップで攻撃力増加
        self.defense += 3  # レベルアップで防御力増加
        self.exp = 0  # 経験値リセット
        print(str(self.name) + "のレベルが" + str(self.level) + "に上がった！\nHPが" + str(self.hp) + "に上がった！\n攻撃力が" + str(self.attack) + "に上がった！\n守備力が" + str(self.defense) + "に上がった！")

hero = Hero("勇者", 30, 5, 5, 10)
#%%
slime = Monster("スライム", 10, 0, 1, 1, 10, 10)
drakey = Monster("ドラキー", 13, 0, 1, 1, 20, 10)
doragon = Monster("ドラゴン", 30, 5, 1, 1, 50, 10)
metalslime= Monster("メタルスライム", 10, 999, 5, 1000, 100, 100)
rikant = Monster("リカント", 100, 20, 20, 20, 100, 100)
dororu = Monster("ドロル", 200, 200, 20, 20, 200, 100)
kimera = Monster("キメラ", 400, 200, 50, 50, 100, 100)
gosuto = Monster("ゴースト", 500, 20, 40, 20, 200, 100)
goldman = Monster("ゴールドマン", 600, 20, 50, 50, 100, 4000)
golem = Monster("ゴーレム", 1000, 0, 70, 200, 1000, 1000)
ryuuou = Monster("りゅうおう", 1000, 200, 80, 100, 1000, 1000)
ryuuou2 = Monster("竜王", 1200, 100, 100, 200, 5000, 5000)
darkdream = Monster("ダークドレアム", 100000, 100, 200, 200, 10000, 10000)
kingslime = Monster("キングスライム", 1000000, 100, 1000, 300, 1000, 10000)
ultoraslime = Monster("ウルトラスライム", 10000000, 1000, 10000, 200, 200, 20000)

import random
monsters1 = [slime, drakey, doragon, metalslime]
appeard_monster = random.choice(monsters1)
monsters2 = [rikant, dororu, kimera, gosuto, golem, metalslime, goldman]
monsters3 = [ryuuou, ryuuou2]
monsters4 = [darkdream]
monsters5 = [kingslime, ultoraslime]

if hero.level >= 40:  # 勇者のレベルが20以上の時
    appeard_monster = random.choice(monsters5)
elif hero.level >= 30: # 勇者のレベルが10以上の時
    appeard_monster = random.choice(monsters4)
elif hero.level >= 20:
    appeard_monster = random.choice(monsters3)
elif hero.level >= 10:
    appeard_monster = random.choice(monsters2)

print(appeard_monster.name + "が現れた！")
while hero.hp > 0:
    print("勇者の攻撃！")

    appeard_monster.hp -= hero.attack

    if appeard_monster.hp > 0:
        print(appeard_monster.name + "は" + str(hero.attack) + "のダメージを受けた！")
        print(" ")

    else:
        print(appeard_monster.name + "は" + str(hero.attack) + "のダメージを受けた！")
        print(appeard_monster.name + "は力尽きた")
        print(" ")
        print("勇者は戦闘に勝った！")

        hero.gain_exp(appeard_monster.exp)

        break
    
    print(appeard_monster.name + "の攻撃！")
    print("勇者は" + str(appeard_monster.attack) + "のダメージを受けた！")
    print(" ")

    #hero.hp -= appeard_monster.attack
    #if hero.hp <= 0:
    #    hero.hp += 10000
    #    print("勇者はせかいじゅのはを使った！\n勇者は生き返った！")
    #if hero.hp < ((hero.hp)*3) / 7:
    #    hero.hp += 30
    #    print("勇者はやくそうを使った！\nHPが30かいふくした！")

else:
    print("勇者は力尽きた")
    print(" ")
    print("勇者は戦闘に負けた！")

#%% 
if hero.gold >= 50:
    hero.attack += 10
    hero.gold -= 50
    print("勇者はひのきのぼうを装備した。")
else:
    print("ひのきのぼうを買うにはお金が足りないようだ。")
#%%
if hero.gold >= 200:
    hero.attack += 20
    hero.gold -= 200
    print("勇者はどうのつるぎを装備した。")
else:
    print("どうのつるぎを買うにはお金が足りないようだ。")
#%%    
if hero.gold >= 1000:
    hero.attack += 50
    hero.gold -= 1000
    print("勇者ははがねのつるぎを装備した。")
else:
    print("はがねのつるぎを買うにはお金が足りないようだ。")

#%%
if hero.gold >= 20000:
    hero.attack += 100
    hero.gold -= 20000
    print("勇者はほのおのつるぎを装備した。")
else:
    print("ほのおのつるぎを買うにはお金が足りないようだ。")

#%%
if hero.gold >= 30000:
    hero.mp += 100
    hero.gold -= 30000
    print("勇者は不思議な木の実を食べた！\n勇者のMPが100上がった！")
else:
    print(" ")

#%%
if hero.level >= 20:
    hero.attack += 500
    hero.gold += 10000
    print("勇者はロトのつるぎを見つけた！\n勇者はロトのつるぎを装備した。\n勇者は10000ゴールドを手に入れた！")
else:
    print(" ")

#%%
if hero.level >= 10:
    hero.gold += 1000
    print("勇者は1000ゴールドを手に入れた！")
else:
    print(" ")

#%%
if hero.mp >= 5:
   hero.hp += 30
   hero.mp -= 5
   print("勇者はホイミをとなえた！\nHPが30かいふくした！")
else:
    print("勇者はホイミをとなえた！\nしかし、MPがたりない！")

#%%
if hero.mp >= 10:
    hero.hp += 100
    hero.mp -= 10
    print("勇者はベホイミをとなえた！\nHPが100かいふくした！")
else:
    print("勇者はベホイミをとなえた！\nしかし、MPがたりない！")

#%%
if hero.mp >= 20:
    hero.attack *= 2
    hero.mp -= 20
    print("勇者はバイキルトをとなえた！\n勇者の攻撃力が2倍に上がった！")
else:
    print("勇者はバイキルトをとなえた！\nしかし、MPがたりない！")

#%%
if hero.mp >= 30:
    hero.hp += 999
    hero.mp -=30
    print("勇者はベホマをとなえた！\nHPが999かいふくした！")
else:
    print("勇者はベホマをとなえた！\nしかし、MPがたりない！")

#%%
if hero.mp >= 10:
    appeard_monster.hp -= 100
    hero.mp -=10
    print("勇者はライデインをとなえた！" + str(appeard_monster.name) + "は100のダメージを受けた！")

#%%
hero_status = ("勇者" + " " + "レベル" + str(hero.level), "HP" + str(hero.hp), "MP" + str(hero.mp), "攻撃力" + str(hero.attack), "守備力" + str(hero.defense),  str(hero.gold) + " G")
print(hero_status)     

#%%
#
# 勇者はギガデインをとなえた！
# 勇者はベホマズンをとなえた！
# 勇者はギガスラッシュをはなった！
# 勇者はマダンテをとなえた！
# 勇者は 