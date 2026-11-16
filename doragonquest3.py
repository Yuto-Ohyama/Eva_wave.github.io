#%%
import random

# モンスタークラス
class Monster:
    def __init__(self, name, hp, mp, attack, defense, exp, gold):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.gold = gold

# 勇者クラス
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

    # 経験値とゴールドを獲得し、レベルアップを判定
    def gain_exp(self, amount_exp, amount_gold):
        self.exp += amount_exp
        self.gold += amount_gold
        print(f"{self.name}は{amount_exp}の経験値と{amount_gold}ゴールドを手に入れた！")

        if self.exp >= 100:  # 100経験値でレベルアップ
            self.level_up()

    # レベルアップ処理
    def level_up(self):
        self.level += 1
        self.hp += 20
        self.mp += 5
        self.attack += 5
        self.defense += 3
        self.exp = 0  # 経験値リセット
        print(f"{self.name}はレベル{self.level}に上がった！\nHP: {self.hp}, 攻撃力: {self.attack}, 守備力: {self.defense}")

    # ステータス表示
    def show_status(self):
        print(f"{self.name} - レベル {self.level}, HP: {self.hp}, MP: {self.mp}, 攻撃力: {self.attack}, 守備力: {self.defense}, ゴールド: {self.gold}G")

# ダメージ計算式（敵の攻撃力と自分の守備力を使用）
def calculate_damage(attacker, defender):
    damage = (attacker.attack / 2) - (defender.defense / 4)
    # ダメージが0未満にならないようにする
    damage = max(1, int(damage))
    return damage

# モンスターを倒した時の処理
def monster_defeated(hero, monster):
    print(f"{monster.name}を倒した！")
    hero.gain_exp(monster.exp, monster.gold)
hero = Hero("勇者", 100, 30, 10, 8)

#%%
# モンスターを作成
slime = Monster("スライム", 10, 0, 12, 2, 10, 10)
drakey = Monster("ドラキー", 13, 0, 14, 3, 20, 10)
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


# ランダムにモンスターが登場
monsters1 = [slime, drakey, doragon, metalslime]
appeard_monster = random.choice(monsters1)
monsters2 = [rikant, dororu, kimera, gosuto, golem, metalslime, goldman]
monsters3 = [ryuuou, ryuuou2]
monsters4 = [darkdream]
monsters5 = [kingslime, ultoraslime]
appeard_monster = random.choice(monsters1)
print(f"{appeard_monster.name}が現れた！")

if hero.level >= 40:  # 勇者のレベルが20以上の時
    appeard_monster = random.choice(monsters5)
elif hero.level >= 30: # 勇者のレベルが10以上の時
    appeard_monster = random.choice(monsters4)
elif hero.level >= 20:
    appeard_monster = random.choice(monsters3)
elif hero.level >= 10:
    appeard_monster = random.choice(monsters2)

# 戦闘ループ
while hero.hp > 0 and appeard_monster.hp > 0:
    # 勇者の攻撃
    print("勇者の攻撃！")
    damage_to_monster = calculate_damage(hero, appeard_monster)
    appeard_monster.hp -= damage_to_monster
    if appeard_monster.hp > 0:
        print(f"{appeard_monster.name}は{damage_to_monster}のダメージを受けた！ 残りHP: {appeard_monster.hp}")
    else:
        monster_defeated(hero, appeard_monster)
        break

    # モンスターの反撃
    print(f"{appeard_monster.name}の攻撃！")
    damage_to_hero = calculate_damage(appeard_monster, hero)
    hero.hp -= damage_to_hero
    print(f"勇者は{damage_to_hero}のダメージを受けた！ 残りHP: {hero.hp}")
    if hero.hp <= 0:
        print("勇者は力尽きた！")
        break

# 勇者のステータス表示
hero.show_status()
#%%