import random

class Hero:
    def __init__(self, name, lvl, health, strength):
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_health = health
        self.hero_strength = strength

    def greet(self):
        print(f"Привет, я {self.hero_name}, мой уровень {self.hero_lvl}")

    def attack(self):
        print(f"{self.hero_name} наносит удар!")
        self.hero_strength -= 1

    def rest(self):
        print(f"{self.hero_name} отдыхает…")
        self.hero_health += 1

class Warrior(Hero):
    def __init__(self, name, lvl, health, strength, stamina):
        super().__init__(name, lvl, health, strength)
        self.stamina = stamina

    def attack(self):
        print('Воин атакует мечом!')

class Mage(Hero):
    def __init__(self, name, lvl, health, strength, mana):
        super().__init__(name, lvl, health, strength)
        self.mana = mana

    def attack(self):
        print('Маг кастует заклинание!')

class Assassin(Hero):
    def __init__(self, name, lvl, health, strength, stealth):
        super().__init__(name, lvl, health, strength)
        self.stealth = stealth

    def attack(self):
        print('Ассасин атакует из-под тишка!')

voin = Warrior('Warrior', 100, 1000, 400, 99)
mag = Mage('Mage', 230, 1000, 200, 500)
asasin = Assassin('Assassin', 101, 1000, 300, 777)

heroes = {
    'Warrior': voin,
    'Mage': mag,
    'Assassin': asasin
}

crash = input('Выберите героя (Warrior / Mage / Assassin): ').capitalize()

if crash in heroes:
    player = heroes[crash]
    enemy = random.choice(list(heroes.values()))

    print(f'Вы выбрали: {player.hero_name}')
    print(f'Противник: {enemy.hero_name}')

    if player == enemy:
        print('Ничья!')
    else:
        winners = {
            'Warrior': 'Assassin',
            'Assassin': 'Mage',
            'Mage': 'Warrior'
        }

        if winners[player.hero_name] == enemy.hero_name:
            print(f'{player.hero_name} победил!')
        else:
            print(f'{enemy.hero_name} победил!')
else:
    print('Такого героя нет!')