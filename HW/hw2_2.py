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
    def rest(self):
        print(f"{self.hero_name} отдыхает")
        self.hero_health += 1

class Warrior(Hero):
    def __init__(self, name, lvl, health, strength, stamina):
        super().__init__(name, lvl, health, strength)
        self.stamina = stamina
    def attack(self):
        print(f"{self.hero_name} атакует мечом!")

class Mage(Hero):
    def __init__(self, name, lvl, health, strength, mana):
        super().__init__(name, lvl, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.hero_name} кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, lvl, health, strength, stealth):
        super().__init__(name, lvl, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.hero_name} атакует из-под тишка!")

heroes = [
    Warrior("Warrior", 100, 1000, 400, 999),
    Mage("Mage", 100, 1000, 200, 999),
    Assassin("Assassin", 100, 1000, 300, 999)
]

winners = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior"
}

choice = input('Введите номер героя (Warrior-1 / Mage-2 / Assassin-3): ')

if choice in ["1", "2", "3"]:
    player = heroes[int(choice) - 1]
    enemy = random.choice(heroes)

    print(f"\nВы выбрали: {player.hero_name}")
    print(f"Противник: {enemy.hero_name}")

    player.attack()
    enemy.attack()

    if player == enemy:
        print("Ничья!")
    elif winners[player.hero_name] == enemy.hero_name:
        print(f"{player.hero_name} победил!")
    else:
        print(f"{enemy.hero_name} победил!")
else:
    print("Такого героя нет!")