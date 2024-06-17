import random

nbres = list(range(0,10))
nbre_cache = random.choice(nbres)

while True: #
    essaie = int(input("Devinez le nombre cache : "))
    if essaie == nbre_cache:
        print("Vous avez trouve")
        break
    elif essaie < nbre_cache:
        print("trop petit, ressayer")
    else:
        print("trop grand, reesayez")
