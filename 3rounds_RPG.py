import random

# Define the weapons and their powers
weapons = {
    "sword": 20,
    "axe": 25,
    "bow": 15
}

# Create the player and enemy objects
player = {
    "name": "Player",
    "points": 100,
    "weapons": weapons.copy()
}
enemy = {
    "name": "Enemy",
    "points": 100,
    "weapons": weapons.copy()
}
print("Your Current Score is 100 & compete with Enemy")
# Start the game
for round in range(3):
    
    # Let the player choose a weapon
    player_weapon = input("Choose your weapon: sword, axe, or bow? ").lower()

    # Let the enemy choose a weapon
    enemy_weapon = random.choice(list(enemy["weapons"].keys()))

    # Calculate the damage dealt
    player_damage = player["weapons"][player_weapon]
    enemy_damage = enemy["weapons"][enemy_weapon]

    # Apply the damage
    player["points"] -= enemy_damage
    enemy["points"] -= player_damage

    # Print the results
    print(f"Round {round + 1}:")
    print(f"Player:  {player['points']} points")
    print(f"Enemy:  {enemy['points']} points")

# Print the winner
if player["points"] > enemy["points"]:
    print("Player wins!")
elif enemy["points"] > player["points"]:
    print("Enemy wins!")
else:
    print("Tie!")
