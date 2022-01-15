def battle_intro():
    print("----------Welcome to BattleScrabble!----------")
    name = input("What's your name? \n")
    age = int(input("What's your age: \n"))
    if age >= 18:
        print("You are eligible to enter the battlefield.")
    else:
        print(f"Hello {name.capitalize()}, aren't you too young.")

def main():
    battle_intro()


if __name__ == '__main__':
    main()