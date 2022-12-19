import random

# 1. ziskani nahodneho slova DONE
# 2. prevod slova na pismena DONE
# 2.5 prevezt pismena na znaky a rict mu kolik ma slovo pismen DONE
# 3. misto kam ulozit uhadnuta pismena DONE
# 4. misto kam ulozit spatna pismena DONE
# 5. zjisteni vyskytu pismena ve slove DONE
# 6. osetrit vstup, pouze pismena z abecedy, srat na cestinu DONE
# na otevirani a cteni souboru pouzit with open("nazevsouboru.txt", v jakem modu to pouzit "r")
hra = True
with open("slova1.txt", "r") as f:
    slova1 = f.readlines()

while hra:
    # slova = ("limetka", "piano", "prsten", "smrt", "vyvrcholeni")
    znak = "-"
    zivoty = 6
    nahodne_slovo = random.choice(slova1).strip("\n")
    rozdeleni = list(nahodne_slovo)
    # print(rozdeleni)
    print("vase slovo ma", len(rozdeleni), "pismen")
    znaky = list(znak * len(rozdeleni))
    hadani = True
    while hadani:
        print(znaky)
        zadano = input("hadej pismeno:")
        zadano = zadano.lower()
        if zadano.isalpha() and len(zadano) > 0:
            zadano = zadano[0]
            if zadano in rozdeleni:
                print("zadal jsi", zadano, "a to je spravne, hadej dal:", "zbyvajici zivoty", zivoty)
                for i in range(len(nahodne_slovo)):
                    if nahodne_slovo[i] == zadano:
                        znaky[i] = zadano
                        rozdeleni.remove(zadano)
            else:
                zivoty -= 1
                print("pismeno", zadano, "neni ve slove, hadej dal:", "zbyvajici zivoty", zivoty)
            if not rozdeleni:
                print("vyhral jsi! hraj znova!\n")
                hadani = False
                continue
        if zivoty == 0:
            print("Prohral jsi :). hraj znova!\n")
            hadani = False
            continue
