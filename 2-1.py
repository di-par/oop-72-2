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

kirito = Hero("Kirito", 99, 1000, 1700)
asuna = Hero("Asuna", 101, 1000, 2000)

kirito.greet()
asuna.greet()

kirito.attack()
print(f"Сила Kirito (-1): {kirito.hero_strength}")
asuna.hero_health -= 1
print(f"Здоровье Asuna (-1): {asuna.hero_health}")

asuna.attack()
print(f"Сила Asuna (-1): {asuna.hero_strength}")
kirito.hero_health -= 1
print(f"Здоровье Kirito (-1): {kirito.hero_health}")

kirito.rest()
print(f'Здоровье Kirito (+1): {kirito.hero_health}')
asuna.rest()
print(f'Здоровье Asuna (+1): {asuna.hero_health}')

kirito.hero_lvl += 1
print(f'Уровень Kirito повышен! {kirito.hero_lvl}')
asuna.hero_lvl += 1
print(f'Уровень Asuna повышен! {asuna.hero_lvl}')