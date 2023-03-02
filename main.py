import world
import character
import enemies

player_name = input('Enter your name and press Enter to start...\n')
print(f"\n\nWake up...\nWake up, {player_name}.\nYou need to go...\n\n\n")

player = character.Character(player_name)
dungeon = world.World()
dungeon.visualistion()