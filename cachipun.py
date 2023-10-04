import numpy as np

def cachipun(p):

    # Definir al bot:
    bot = ["tijera", "papel", "piedra"]
    c = np.random.choice(bot)

    if c == p:
        print(f"Bot: {c}\n\n")
        print("------------------------- ¡Empate! -------------------------\n\n")
        v = input("Elija de nuevo: piedra, papel o tijera:\n\nJugador: ").lower()
        return cachipun(v)


    # Bot: tijera
    elif c == "tijera" and p == "papel":
        print(f"Bot: {c}\n\nGana el Bot.") # bot: tijera, player: papel

    elif c == "tijera" and p== "piedra":
        print(f"Bot: {c}\n\nGana el Jugador.") # bot: tijera, player: piedra


    # Bot: papel
    elif c == "papel" and p == "tijera":
        print(f"Bot: {c}\n\nGana el Jugador") # bot: papel, player: tijera

    elif c == "papel" and p == "piedra":
        print(f"Bot: {c}\n\nGana el Bot") # bot: papel, player: piedra


    # Bot: piedra
    elif c == "piedra" and p == "tijera":
        print(f"Bot: {c}\n\nGana el Bot") # bot: piedra, player: tijera

    elif c == "piedra" and p == "papel":
        print(f"Bot: {c}\n\nGana el Jugador") # bot: piedra, player: papel

j1 = input("Elija y escriba: piedra, papel o tijera:\n\nJugador: ").lower()

try:
    j1 = str(j1)
    if j1 is not None:
        if j1 == "piedra" or j1 == "papel" or j1 == "tijera":
            cachipun(j1)
        else:
            print("\nError: el usuario usó ALGÚN truco.")

except ValueError:
    print("\nError: el usuario usó ALGÚN truco.")
