def print_colored(text, color="reset", style=None):
    # Dictionary mapping color names to their ANSI color codes
    colors = {
        # Normal (Standard) 8 Colors
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        
        # High-Intensity (Bright) 8 Colors
        "bright_black": "90",
        "bright_red": "91",
        "bright_green": "92",
        "bright_yellow": "93",
        "bright_blue": "94",
        "bright_magenta": "95",
        "bright_cyan": "96",
        "bright_white": "97",
        
        # Reset marker
        "reset": "0"
    }
    
    # Dictionary mapping text styles to their ANSI style codes
    styles = {
        "bold": "1",
        "dim": "2",
        "underline": "4"
    }
    
    # Look up codes (default to empty if not found)
    color_code = colors.get(color.lower(), "0")
    style_code = styles.get(style.lower(), "") if style else ""
    
    # Combine style and color if both are present
    if style_code and color_code != "0":
        ansi_sequence = f"\033[{style_code};{color_code}m"
    elif style_code:
        ansi_sequence = f"\033[{style_code}m"
    else:
        ansi_sequence = f"\033[{color_code}m"
        
    reset_code = "\033[0m"
    
    # Print with the combined style/color and reset at the end
    print(f"{ansi_sequence}{text}{reset_code}")

# od Kuby Poláka na barevný text (Multiplayerjake), nic z toho není moje práce. (to nahoře)

from time import sleep

#from playsound3 import playsound

import random

look_around = False
shed_visited = False
waterfall_visited = False
ruby_crystal_obtained = False
staircase_visited = False
inventory = []
health = 100
max_health = 100
base_dmg = 20
skeleton_uno_health = 50
skeleton_duo_health = 50
skeleton_dmg = 12

def ask():
    choice = input("What do you want to do?")
    return choice

def valid_ask(valid_choices):
    choice = ask()

    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = ask()

    return choice


def player_death():
    if health <= 0:
        print_colored("You died!", style="bold", color="red")
        input("\nPress Enter to exit the game...")
        return True
    return False

def show_inventory():
    print("\n===== INVENTORY =====")

    if not inventory:
        print("Your inventory is as empty as it gets.")
    else:
        for item in inventory:
            print(f"- {item}")

    print("=====================")


def show_health():
    print_colored(f"You have {health} health.", style="bold", color="red")

    return

def player_damage():
    dmg = base_dmg

    if "Sword" in inventory:
        dmg += 10

    return dmg



def obtain_ruby_crystal():
    global health, max_health, ruby_crystal_obtained
    ruby_crystal_obtained = True

    inventory.append("Ruby Crystal")

    max_health += 25
    health += 25

    print("\nYou obtained a heart-shaped \033[31mRuby Crystal\033[0m!")
    print(f"Maximum HP increased to {max_health}!")
    print(f"Current HP: {health}/{max_health}")


def sudo_install_opsec(): #main funkce, neboli start
    print("You have heard rumors about a legendary treasure called the Azure Latch.")
    print("It is said to be hidden somewhere inside this abandoned castle.")
    print("Nobody has ever managed to find it, but you are determined to try.")
    print("\n\033[32m=== The Ruined Castle ===\033[0m")
    print("You stand infront of a castle, broken down by time.")
    print("1) Enter the castle   2) Look around the castle")
    choice = valid_ask(["1", "2"])

    if choice == "1":
        ruined_castle_enter()
    elif choice == "2":
        ruined_castle_look()
   # else:
    #    print("Invalid choice. Please choose 1 or 2.")
    #    udelal jsem funkci, ktera to cely vyresila takze jsem to proste dal pryc

def start_game():
    sudo_install_opsec()


def ruined_castle_look():
    print("\nYou decided to look around the castle.")
    sword_chance = random.randint(1,5)

    if sword_chance >= 2:
        print("You found a \033[33mSword\033[0m!")
        inventory.append("Sword")
        #print(f"Your iventory currently looks like this: {inventory}") stary inventory reading, udelal jsem funkci aby to bylo praktictejsi
        show_inventory()
        ruined_castle_enter()
    elif sword_chance < 5:
        print("You didnt find anything worthwhile.")
        ruined_castle_enter()

def ruined_castle_enter():
    print_colored("\nYou slowly open the gate to the castle.", style="bold", color="bright_black")
    sleep(2)
    #playsound("C:\\Users\\Tobias\\Desktop\\Python\\alex_jauk-squeaky-gate-noise-227014.mp3")
    print("\nYou entered the ruined castle, you see a giant staircase in front of you. There are also two doors. One on the left and one on the right.")
    print("1) Enter the left door  2) Go up the staircase  3) Enter the right door ")
    choice = valid_ask(["1", "2", "3"])
    if choice == "1":
        left_door()
    elif choice == "2":
        staircase()
    elif choice == "3":
        right_door()

def staircase():
    global staircase_visited
    staircase_visited = True
    print("\nYou walk up the staircase, theres a glowing box in front of you.")
    #playsound("C:\\Users\\Tobias\\Desktop\\Python\\freesound_community-steps-on-stairs-102729.mp3")
    print("Open it?")
    print("1) Yes")
    print("2) No")
    choice = valid_ask(["1", "2"])

    if choice == "1":
        obtain_ruby_crystal()
        #print(f"Your inventory currently looks like this: {inventory}")  stary inventory reading, udelal jsem funkci aby to bylo praktictejsi x2
        show_inventory()
        #playsound("C:\\Users\\Tobias\\Desktop\\Python\\mixkit-unlock-new-item-game-notification-254.wav")
        ruined_castle_enter_crystal()
    if choice == "2":
        print("You chose not to open the glowing box.")
        ruined_castle_enter_crystal()


def right_door():
    print("\nYou have entered the right door.")
    print("The room is surrounded in complete darkness, walk forward?")
    print("1) Yes")
    print("2) No")
    choice = valid_ask(["1", "2"])

    if choice == "1":
        right_door_death()
    elif choice == "2":
        ruined_castle_enter_RD()


def skeleton_fight():
    print("The skeletons are burning with rage! They draw their spears and initiate combat.")
    global skeleton_duo_health, skeleton_uno_health, health
    while skeleton_uno_health > 0 or skeleton_duo_health > 0:
       
       
        if skeleton_uno_health >0:
            print_colored(f"\nSkeleton 1 HP: {skeleton_uno_health}", style="bold")
        else:
            print_colored("Skeleton 1 HP: DEAD", style="bold", color="bright_black")
        if skeleton_duo_health >0:
            print_colored(f"Skeleton 2 HP: {skeleton_duo_health}", style="bold")
        else:
            print_colored("Skeleton 2 HP: DEAD", style="bold", color="bright_black")
        damage = player_damage()

        print("\nWho do you want to attack?")
        valid_targets = []

        if skeleton_uno_health >0:
            print_colored("1) Skeleton 1", style="bold",)
            valid_targets.append("1")

        if skeleton_duo_health >0:
            print_colored("2) Skeleton 2", style="bold",)
            valid_targets.append("2")

        
        choice = valid_ask(valid_targets)
        if choice == "1":
            skeleton_uno_health -= damage
            #playsound("C:\\Users\\Tobias\\Desktop\\Python\\JDSherbert - Pixel Game Essentials SFX Pack (FREE)\\Stereo\\mp3\\JDSherbert - Pixel Game Essentials SFX Pack - Damage 1.mp3")
        elif choice == "2":
            skeleton_duo_health -= damage
            #playsound("C:\\Users\\Tobias\\Desktop\\Python\\JDSherbert - Pixel Game Essentials SFX Pack (FREE)\\Stereo\\mp3\\JDSherbert - Pixel Game Essentials SFX Pack - Damage 1.mp3")
        if skeleton_uno_health > 0:
            health -= skeleton_dmg
        if skeleton_duo_health > 0:
            health -= skeleton_dmg
        if skeleton_uno_health > 0 and skeleton_duo_health > 0:
            print_colored("Both skeletons stab you with their spears! You took 24 dmg!", color="green")
            show_health()
        elif skeleton_uno_health > 0 or skeleton_duo_health > 0:
            print_colored("The last skeleton stands his ground and stabs you with its spear! You took 12 dmg!", color="cyan")
            show_health()
        if player_death():
            break
        if skeleton_uno_health <= 0 and skeleton_duo_health <= 0:
            print_colored("\nYou defeated both skeletons! Hooray!", style="bold", color="yellow")
            left_door_end()
            break

def left_door():
    print("\nYou have entered the left door.")
    print("You walk forward and see two skeletons with spears.")
    print("They slowly approach you...")
    skeleton_fight()

def right_door_death():
    global health
    print("You went forward and fell down to your death, impaled by spikes. All shrouded in darkness.")
    health -= 200
    player_death()



def ruined_castle_enter_RD():
    while True:
        print("\nYou close the right door and come back to the same spot. Which place do you choose this time? ")
        print("1) Enter the left door  2) Go up the staircase  3) Enter the right door ")
        choice = valid_ask(["1", "2", "3"])
        if choice == "1":
            left_door()
            break
        elif choice == "2":
            if staircase_visited == False:
                staircase()
                break
            else:
                print_colored("\nYou have already gone up the staircase.", style="bold", color="bright_black")
        elif choice == "3":
            print("\nYou decide to enter the right door again.")
            print("The room is surrounded in complete darkness, walk forward?")
            print("1) Yes")
            print("2) No")

            choice = valid_ask(["1", "2"])

            if choice == "1":
                right_door_death()
                return
    

def ruined_castle_enter_crystal():
    print("Your path forward is obfuscated by fallen debris. You turn back.")
    print("\nYou come down the stairs back to where you were before, which door do you enter?")
    print("1) Enter the left door  2) Enter the right door ")
    choice = valid_ask(["1", "2"])
    if choice == "1":
        left_door()
    elif choice == "2":
        right_door()

def left_door_end():
    global health, max_health
    print("\nYou walk past the remains of the skeletons.")
    print("You walk into a huge cave, you can't see anything.")
    if ruby_crystal_obtained == True:
        print("\nSacrifice the \033[31mRuby Crystal\033[0m to light up the cave?")
        print("1) Yes")
        print("2) No")
        choice = valid_ask(["1", "2"])
        if choice == "1":
            print("\nYou sacrifice the crystal, lighting up the cave, it reveals a waterfall, a shed and a mysterious door.")
            inventory.remove("Ruby Crystal")
            max_health -= 25
            if health > max_health:
                health = max_health       
            print(f"Maximum HP decreased to {max_health}!")
            show_health()
            visible_cave()
        elif choice == "2":
            dark_cave()
    else: dark_cave()

def dark_cave():
    global health
    print("Where do you want to go?")
    print("1) ???  2) ???  3) ???")
    choice = valid_ask(["1", "2", "3"])
    if choice == "1":
        print_colored("\nYou walk into the darkness and hear the sound of flowing water.", style="bold", color="bright_black")
        print("You walk towards the sound and trigger a trap, a gemstone falls from the ceiling and impales you.")
        health -= 200
        player_death()
    elif choice == "2":
        randint = random.randint(1, 100)
        if randint >= 90:
            print_colored("You got extremely lucky and the gemstones above started to shine, lighting up the cave.", style="bold", color="magenta")
            visible_cave()
        else:
            print_colored("\nYou walk into the dark blindly.", style="bold", color="bright_black")
            print("You accidentally press a button on the side of a wooden shed.")
            print("Arrows fly out from the wall, piercing your body, making you bleed to death.")
            health -= 200
            player_death()
    elif choice == "3":
        print_colored("\nYou walk into the darkness and can slightly make out a door right infront of you with a golden keyhole.", style="bold", color="bright_black")
        print("You try to open it, but its locked.")
        print("You hear a mechanical switch trigger and the floor makes spikes come out that pierce your body, killing you.")
        health -= 200
        player_death()
        
def visible_cave():
    while True:
        print("1) Waterfall  2) Shed  3) Mysterious door")
        choice = valid_ask(["1", "2", "3"])
        if choice == "1":
            if waterfall_visited == True:
                print_colored("\nYou have already visited the waterfall.", style="bold", color="bright_black")
            else:
                waterfall()
        elif choice == "2":
            if shed_visited == True:
                print_colored("\nYou have already visited the shed.", style="bold", color="bright_black")
            else:
                shed()
        elif choice == "3":
            mystery_door()
            return

def mystery_door():
    global health
    print("\nYou walk towards the mysterious door, it has a golden keyhole on it.")
    if "Golden Key" in inventory:
        print("You use the \033[33mGolden Key\033[0m to open the door.")
        inventory.remove("Golden Key")
        show_inventory()
        print("\nThe door opens, revealing a dungeon room, with two iron cells. One of them was forced open, and the other is locked.")
        dungeon_room()
    else:
        print("\nYou try to open it, but its locked.")
        print("You hear a mechanical switch trigger and the floor makes spikes come out that pierce your body, killing you.")
        health -= 200
        player_death()

def waterfall():
    global health, waterfall_visited
    print("\nYou walk towards the waterfall, and drink some water.")
    print_colored("The water has a magical effect and it heals you!", color="bright_green")
    waterfall_visited = True
    health += 100
    if health > max_health:
        health = max_health
    print(f"HP increased to {health}!")
    show_health()
    print("You leave the waterfall and go back to the start of the cave.")
    print("\n")

def shed():
    global shed_visited
    shed_visited = True
    print("\nYou walk towards a broken down shed.")
    print("You step inside and find a key on the table")
    print("Pick it up?")
    print("1) Yes")
    print("2) No")
    choice = valid_ask(["1", "2"])
    if choice == "1":
        print("You found a \033[33mGolden Key\033[0m!")
        inventory.append("Golden Key")
        show_inventory()
        print("You leave the old shed and go back to the start of the cave.")
        print("\n")
    elif choice == "2":
        print("You chose not to pick up the key.")
        print("You leave the old shed and go back to the start of the cave.")
        print("\n")

def dungeon_room():
    global health, look_around
    while True:
        print("\nDo you want to look around the dungeon room or walk forward?")
        print("1) Look around  2) Walk forward")
        choice = valid_ask(["1", "2"])
        if choice == "1":
            if look_around == True:
                print_colored("\nYou have already looked around the dungeon room.", style="bold", color="bright_black")
            elif look_around == False:
                print("\nYou look around the dungeon room and find a chest.")
                print("Open it?")
                print("1) Yes")
                print("2) No")
                choice = valid_ask(["1", "2"])
                if choice == "1":
                    randint = random.randint(1, 10)
                    if randint >= 4:
                        print("\nYou found a \033[33mHeal Potion\033[0m!")
                        inventory.append("Heal Potion")
                        show_inventory()
                        look_around = True
                    else:
                        print("\nThe chest erupts in a dark blue mist, and you feel your body being drained of life.")
                        health -= 200
                        player_death()
                        return
                elif choice == "2":
                    print("\nYou chose not to open the chest.")
        elif choice == "2":
            dungeon_room2()
            return

def opened_door_D2():
    print("\nYou open the door and find the rumors about the Azure Latch to be true, a treasure chest filled with gold and jewels.")
    print_colored("You have completed the game! Congratulations!", style="bold", color="yellow")
    sleep(3)
    print_colored("\nThe game hasn't ended yet.", style="bold", color="bright_black")
    sleep(2)
    ruined_king_bossfight()

def dungeon_room2():
    print("\nYou walk forward and find a door.")
    print("Open it?")
    print("1) Yes")
    print("2) No")
    choice = valid_ask(["1", "2"])
    if choice == "1":
        opened_door_D2()
    elif choice == "2":
        print("\nYou chose not to open the door.")
        print("1) ???")
        choice = valid_ask(["1"])
        if choice == "1":
            print("\nYou find a writing on the wall: 'The Azure Latch is a lie.'")
            dungeon_room2nodoor()


def dungeon_room2nodoor():
    print("You walk back to the door, determined to find the Azure Latch anyway.")
    print("Open it?")
    print("1) Yes")
    choice = valid_ask(["1"])
    if choice == "1":
        opened_door_D2()

def ruined_king_bossfight():
    global health
    print("\nThe Ruined King rises from the dead and attacks you, he is furious that you have taken his treasure.")
    print("The Ruined King has 200 HP and does 20 damage per attack.")
    ruined_king_health = 200
    while ruined_king_health > 0:
        print_colored("\n•❅───✧❅The Ruined King.❅✧───❅•", style="bold", color="green")
        print_colored(f"HP: {ruined_king_health}", style="bold")
        damage = player_damage()
        print("\nDo you want to attack the Ruined King?")
        print("1) Attack")
        if "Heal Potion" in inventory:
            print("2) Use Heal Potion")
            choice = valid_ask(["1", "2"])    
        else:
            choice = valid_ask(["1"])
        if choice == "1":
            ruined_king_health -= damage
            print_colored(f"\nYou attacked the Ruined King for {damage} damage!", color="yellow")
            if ruined_king_health <= 0:
                print_colored("\nYou defeated the Ruined King! Hooray!", style="bold", color="yellow")
                print_colored("\nYou have completed the game! Congratulations!", style="bold", color="yellow")
                input("\nPress Enter to exit the game...")
                break
            health -= 20
            print_colored("\nThe Ruined King attacks with pure anger, dealing 20 damage!", color="green")
            show_health()
            if player_death():
                print_colored("\nMaybe consider looking around for more items.", style="bold", color="red")
                break
            

            
        elif choice == "2":
            print("\nYou used a Heal Potion and restored 80 HP!")
            health += 80
            if health > max_health:
                health = max_health
            inventory.remove("Heal Potion")
            show_health()
            health -= 20
            print_colored("\nThe Ruined King attacks with pure anger, dealing 20 damage!", color="green")
            show_health()
            if player_death():
                print_colored("\nMaybe consider looking around for more items.", style="bold", color="red")
                break

start_game()