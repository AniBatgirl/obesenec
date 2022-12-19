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
    znak = "-"
    zivoty = 6
    pokus = 0
    spravny_pokus = 0
    uspesnost = 0
    spatne = []
    nahodne_slovo = random.choice(slova1).strip("\n")
    rozdeleni = list(nahodne_slovo)
    # print(rozdeleni)
    print("Tvoje slovo má", len(rozdeleni), "písmen")
    znaky = list(znak * len(rozdeleni))  # nahradi hadane slovo -
    hadani = True

    while hadani:
        print(znaky)
        zadano = input("hádej písmeno:")
        zadano = zadano.lower()

        if zadano.isalpha() and len(zadano) > 0:
            pokus += 1
            zadano = zadano[0]

            if zadano in rozdeleni:  # kdyz uhodnuto spravne pismeno
                spravny_pokus += 1
                print("zadal jsi", zadano, "a to je správně, hádej dál:", "zbývající životy:", zivoty, "\n")
                print("špatně zadaná písmena :", spatne)

                for i in range(len(nahodne_slovo)):
                    if nahodne_slovo[i] == zadano:
                        znaky[i] = zadano
                        rozdeleni.remove(zadano)
            else:  # kdyz uhodnuto spatne pismeno
                if zadano not in spatne:
                    spatne.append(zadano)
                else:
                    print("to už jsi zkoušel, -1 život")
                zivoty -= 1
                print("písmeno", zadano, "není ve slově, hádej dál:", "zbývající životy:", zivoty, "\n")
                print("špatně zadaná písmena :", spatne)

            if not rozdeleni:  # pokud uhadnuta vsechna pismena
                uspesnost = spravny_pokus/pokus*100
                print("Vyhrál jsi! hraj znova! tvůj celkový počet pokusů byl", pokus,
                      "a míra úspěšnosti=", uspesnost, "\n")
                hadani = False
                continue

        if zivoty == 0:  # pokud nezbyvaji zadne zivoty
            print("Prohrál jsi :). hraj znova! tvůj celkový počet pokusů byl", pokus,
                  "a míra úspěšnosti=", uspesnost,  "\n")
            hadani = False
            continue
