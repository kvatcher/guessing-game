import random
import time

def ask_user():
    answer = input("Do you want to keep playing? YES/NO ").lower().strip()
    try:
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Try again.")
            return ask_user()
    except Exception as error:
        print("There was a misinput.")
        print(error)
        return ask_user()
    
best_time = 100.0
attempts_record = 10
def game(lives):
    global best_time, attempts_record
    try = 0
    start = time.perf_counter()
    number = random.randint(1,100)
    print("Guess the number!")
    while lives > 0:
        try:
            guess = int(input(""))
        except ValueError as error:
            print("Type in a correct number.")
            guess = int(input(""))
        if guess == number:
            end = time.perf_counter()
            duration = (end-start)
            print(f"You win! The number is {number}. The game ends in {duration:.1f} seconds")
            if duration < best_time:
                print(f"New time record!. Previous record was {best_time}.")
                best_time = duration
            if try < attempts_record:
                print(f"New attempts records with {try} attempts to win! Previous best was {attempts_record}.")
                attempts_record = try
            break
        elif guess > number:
            try+=1
            print("Try again. It's a number lower than what you guessed")
            if guess-number>50:
                print("You are VERY far from guessing!")
            elif guess-number<20:
                print("Getting closer!")
            lives-=1
        elif guess < number:
            try+=1
            print("Try again. It's a number greater than what you guessed")
            if number - guess > 50:
                print("You are VERY far from guessing!")
            elif number - guess < 20:
                print("Getting closer!")
            lives-=1
    if lives == 0:
        print("You lose.")
    if ask_user() == True:
        welcome()

def welcome():
    print("""
        I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.
          Choose difficulty:
          1. Easy (10 tries)
          2. Medium (5 tries)
          3. Hard (3 tries)
          """)
    diff = None
    while not diff:
        try:
            diff = int(input(""))
        except ValueError:
            print("It has to be a number between 1 and 3")
    match diff:
        case 1:
            game(10)
        case 2:
            game(5)
        case 3:
            game(3)
        case _:
            print("Try again.")
            welcome()
    
welcome()
