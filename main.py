import random
# 1. ziskani nahodneho slova DONE
# 2. prevod slova na pismena DONE
# 2.5 prevezt pismena na znaky a rict mu kolik ma slovo pismen DONE
# 3. misto kam ulozit uhadnuta pismena
# 4. misto kam ulozit spatna pismena
# 5. zjisteni vyskytu pismena ve slove
# 6. osetrit vstup, pouze pismena z abecedy, srat na cestinu

slova = ("limetka", "piano", "prsten", "smrt", "vyvrcholeni")
znak = ("-")

nahodne_slovo = random.choice(slova)

rozdeleni = list(nahodne_slovo)

print(rozdeleni)
print("vase slovo ma", len(rozdeleni), "pismen")
print(znak * len(rozdeleni))

zadano = input("hadej pismeno:")
zadano = zadano.lower()[0]

# if zadano:






