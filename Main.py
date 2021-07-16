import random


def walk():
    global blocks_moved
    global blocks_limit
    if blocks_moved < blocks_limit:
        print("You moved 1 block")
        print(f"You're on block {blocks_moved} now.")
        blocks_moved += 1
        event_random = random.randint(1, 10)
        if event_random == 1:
            dungeon()
        elif event_random == 2:
            ore_mine()
        elif event_random == 3:
            gem_mine()
        elif event_random == 4:
            pass
        else:
            pass
    else:
        print("You cannot move any more blocks type quit to end game")


def player_health_check():
    if player_health <= 0:
        print("Your health is 0")
    else:
        print(f"Your health is {player_health}")


def ore_mine():
    while True:
        entering_choice = input("You found a ore mine type (Y) to enter and (N) to skip: ")
        entering_choice = entering_choice.lower()

        if entering_choice == "y":
            ore_or_gem_mine(ores)
            break
        elif entering_choice == "n":
            print("You skipped the mine")
            break
        else:
            print("Invalid input.")


def gem_mine():
    while True:
        entering_choice = input("You found a gem mine type (Y) to enter and (N) to skip: ")
        entering_choice = entering_choice.lower()

        if entering_choice == "y":
            ore_or_gem_mine(gem)
            break
        elif entering_choice == "n":
            print("You skipped the mine")
            break
        else:
            print("Invalid input.")


def ore_or_gem_mine(item_list):
    global score

    ore_or_gem_found = random.choice(item_list)
    ore_or_gem_found_index = item_list.index(ore_or_gem_found)
    amount_found = random.randint(1, 10)

    points_gained = ((ore_or_gem_found_index + 1) * 10) * amount_found
    score += points_gained

    print(f"You found x{amount_found} {ore_or_gem_found}")
    print(f"You gained {points_gained} points and your new score is {score}")


def dungeon():
    global score
    global player_attack_damage
    global player_health
    global player_critical_chance
    global player_critical_damage
    global player_dodge_fail_chance
    points_earned = 0
    game_over = False

    print("You encountered a dungeon")

    while not game_over:

        while True:
            entering_choice = input("Type (Y) if you want to enter the dungeon or (N) if you want to skip it: ")
            entering_choice = entering_choice.lower()
            if entering_choice == "y":
                start_dungeon = True
                break
            elif entering_choice == "n":
                start_dungeon = False
                break
            else:
                print("""Invalid Input type "y" to enter and "n" to skip.""")

        if start_dungeon:
            event_difficulty = random.randint(1, 3)  # Number between 1 and 3 including 1 and 3.
            mob_health = 100 * event_difficulty
            mob_attack = 10 * event_difficulty
            print(f"Mob Health: {mob_health}")
            print(f"Mob Attack: {mob_attack}")
            while True:
                if mob_health == 0:
                    print("You defeated the boss")
                    points_earned += 50*event_difficulty
                    score += points_earned
                    print(f"You gained {points_earned} and now your score is {score}")
                    game_over = True
                    break
                elif player_health <= 0:
                    print("You failed dungeon")
                    points_earned += 5 * event_difficulty
                    score += points_earned
                    print(f"You gained {points_earned} and now your score is {score}")
                    game_over = True
                    break
                else:
                    player_move = input("""Type "d" to dodge and "a" to attack >""")
                    player_move = player_move.lower()
                    mob_move = random.randint(1, 4)  # 1 is attack, 2 is dodge, 3 is no move
                    if player_move == "d":
                        player_dodge_fail_chance = random.randint(10, 100)
                        if mob_move == 1:
                            if player_dodge_fail_chance <= 10:
                                player_health -= mob_attack
                                print(f"You failed to dodge fully and suffered {mob_attack} damage.")
                            else:
                                print("You dodged the attack!")
                        if mob_move == 2:
                            print("Nothing happened.")
                        if mob_move >= 3:
                            print("Nothing happened.")
                    if player_move == "a":
                        player_critical_chance = random.randint(10, 100)
                        if mob_move == 1:
                            player_health -= mob_attack
                            if player_critical_chance <= 10:
                                mob_health -= player_critical_damage
                                print(f"You both attacked and you dealt {player_critical_damage} damage to mob.")
                                player_health_check()
                                print(f"Mob health is {mob_health}")
                            else:
                                mob_health -= player_attack_damage
                                print(f"You attacked mob and dealt {player_attack_damage} damage.")
                                player_health_check()
                                print(f"Mob health is {mob_health}")
                        if mob_move == 2:
                            print("Mob dodged your attack")
                        if mob_move >= 3:
                            if player_critical_chance <= 10:
                                mob_health -= player_critical_damage
                                print(f"You attacked mob and dealt {player_critical_damage} damage.")
                                player_health_check()
                                print(f"Mob health is {mob_health}")
                            else:
                                mob_health -= player_attack_damage
                                print(f"You attacked mob and dealt {player_attack_damage} damage.")
                                player_health_check()
                                print(f"Mob health is {mob_health}")
                    else:
                        print("""Invalid input your can type "a" to attack and "d" to dodge """)
        else:
            break


blocks_limit = 100
player_health = 10
score = 0
blocks_moved = 1
player_attack_damage = 20
player_critical_chance = 0
player_critical_multiplier = 3
player_critical_damage = player_attack_damage * player_critical_multiplier
player_dodge_fail_chance = 0
ores = ["copper", "iron", "silver", "gold", "uranium", "platinum"]
gem = ["tanzanite", "black opal", "emerald", "ruby", "diamond"]

print("Type help for the list of commands.")

while player_health >= 1:

    player_input = input("> ")
    player_input = player_input.lower()

    if player_input == "help":
        print("""
        help - Gives your lists of commands
        quit - Quit game
        walk - Walk 1 block 
        score - To get your current score
        health- To check your health
        inv - To check your inventory 
        """)
    elif player_input == "walk":
        walk()
    elif player_input == "score":
        print(f"Your current score is {score}")
    elif player_input == "health":
        print(f"Your current health is {player_health}")
    elif player_input == "quit":
        print(f"Your final score is {score}")
        high_score = score
        break
    else:
        print("Invalid input! Type help for the list of commands")
else:
    print("You died! GAME OVER")
