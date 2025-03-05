import random
import time


def ask_user():
    answer = input("Queres seguir jugando? SI/NO ").lower().strip()
    try:
        if answer == 'si':
            return True
        elif answer == 'no':
            return False
        else:
            print("Intente de vuelta.")
            return ask_user()
    except Exception as error:
        print("Hubo un error en lo que ingresó.")
        print(error)
        return ask_user()
    
best_time = 100.0
attempts_record = 10
def game(lives):
    global best_time, attempts_record
    intentos = 0
    start = time.perf_counter()
    numero = random.randint(1,100)
    print("Adiviná el número")
    while lives > 0:
        try:
            guess = int(input(""))
        except ValueError as error:
            print("Ingrese un número.")
            guess = int(input(""))
        if guess == numero:
            end = time.perf_counter()
            duration = (end-start)
            print(f"Ganaste! El número era {numero}. Se termina el juego en {duration:.1f} segundos")
            if duration < best_time:
                print(f"Nuevo récord de tiempo. El récord anterior era {best_time}")
                best_time = duration
            if intentos < attempts_record:
                print(f"Nuevo récord de intentos con {intentos} intentos para ganar! El anterior era {attempts_record}")
                attempts_record = intentos
            break
        elif guess > numero:
            intentos+=1
            print("Intentalo de vuelta, es un número menor al que elegiste")
            if guess-numero>50:
                print("Parece que estás MUY lejos del resultado!")
            elif guess-numero<20:
                print("Te estás acercando al resultado!")
            lives-=1
        elif guess < numero:
            intentos+=1
            print("Intentalo de vuelta, es un número mayor al que elegiste")
            if numero - guess > 50:
                print("Estás MUY lejos del resultado!")
            elif numero - guess < 20:
                print("Te estás acercando!")
            lives-=1
    if lives == 0:
        print("Perdiste.")
    if ask_user() == True:
        welcome()

def welcome():
    print("""
        Estoy pensando en un número del 1 al 100
          Seleccioná la dificultad del juego:
          1. Fácil (10 chances)
          2. Medio (5 chances)
          3. Difícil (3 chances)
          """)
    diff = None
    while not diff:
        try:
            diff = int(input(""))
        except ValueError:
            print("Tiene que ser un número del 1 al 3")
    match diff:
        case 1:
            game(10)
        case 2:
            game(5)
        case 3:
            game(3)
        case _:
            print("Intente de vuelta")
            welcome()
    
welcome()