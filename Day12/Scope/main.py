################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope:
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global scope:
player_health = 10

def game():
    def check_health():
        print(player_health)

    check_health()

print(player_health)

# There is no block scope
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

# Modifying global scope

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

# Global scope variables can be created after the funtion definition which is using it within

enemies = 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@xy_z"
