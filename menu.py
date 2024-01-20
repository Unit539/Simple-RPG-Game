from player import Player
from enemy import Enemy
from random import randint

def menu():
    menu = ["1. Fight", "2. View statistics", "3. Exit"]
    while True:
        print("----------------Menu---------------")
        for item in menu:
            print(item)
        print("-----------------------------------")

        try:
            choise = int(input("Enter number: "))

            if choise == 1:
                fight()
            elif choise == 2:
                stats()
            else:
                print("Exiting game!")
                break
        except NameError:
            print("Enter number")
        except SyntaxError:
            print("Enter number")

def fight():
    fight_menu = ["1. Hit", "2. Heal"]
    while e.hp > 0:
        print(f"Your hp: {p.hp} damage: {p.damage}")
        print(f"Enemy hp: {e.hp} damage: {e.damage}")

        print("---------------------------")
        for item in fight_menu:
            print(item)
        print("---------------------------")

        choise = int(input("Enter number: "))

        if choise == 1:
            e.hp -= p.damage
            print(f"You hit the enemy, he has left {e.hp} hp.")
            p.hp -= e.damage
            print(f"The enemy hit you, you have left {p.hp} hp.\n")
        elif choise == 2:
            rand = randint(1, 5)
            p.hp += rand
            if p.hp > 100:
                p.hp = 100
            
            print(f"You are cured by {rand}. Your current hp is {p.hp}\n")
        else:
            print("Waiting for choise!\n")

        if p.hp < 0:
            print("You lost!\n")
            break

        if e.hp < 0: 
            print("You win!\n")
            break

def stats():
    print("---------------Player stats--------------")
    print(f"Hp: {p.hp}")
    print(f"Damage: {e.damage}")
    print("-----------------------------------------")
    input("Press Enter to continue.")

if __name__ in "__main__":
    p = Player()
    e = Enemy()

    menu()