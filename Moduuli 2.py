#tein 2. Muuttujat ja vuorovaikutteiset ohjelmat & 3. Valintarakenne (if)
name = input("Anna nimesi: ")
print(f"Terve, {name}!")
print("")
import math

r = float(input("Anna ympyrän säde: "))
area = math.pi * r * r
print(f"Ympyrän pinta-ala on {area:.2f}")
print("")
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print(f"Suorakulmion piiri on {piiri:.2f}")
print(f"Suorakulmion pinta-ala on {pinta_ala:.2f}")
print("")
a = int(input("Anna 1. kokonaisluku: "))
b = int(input("Anna 2. kokonaisluku: "))
c = int(input("Anna 3. kokonaisluku: "))

summa = a + b + c
tulo = a * b * c
keskiarvo = summa / 3

print(f"Summa: {summa}")
print(f"Tulo: {tulo}")
print(f"Keskiarvo: {keskiarvo:.2f}")
print("")
leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))

# Muunnos grammoiksi
total_luoti = (leiviska * 20 * 32) + (naula * 32) + luoti
total_grams = total_luoti * 13.3

kg = int(total_grams // 1000)
g = total_grams - kg * 1000  # voi sisältää desimaaleja, koska 13.3 g

print(f"Massa on {kg} kg ja {g:.1f} g (yhteensä {total_grams:.1f} g)")
print("")
import random

# 3-numeroinen koodi, numerot 0..9
koodi3 = ""
for _ in range(3):
    koodi3 += str(random.randint(0, 9))

# 4-numeroinen koodi, numerot 1..6
koodi4 = ""
for _ in range(4):
    koodi4 += str(random.randint(1, 6))

print("3-numeroinen koodi (0..9):", koodi3)
print("4-numeroinen koodi (1..6):", koodi4)
print("")
pituus = int(input("Anna kuhan pituus (cm): "))

minimi = 37
if pituus < minimi:
    puuttuu = minimi - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Puuttuu {puuttuu} cm.")
else:
    print("Kuha on sallittua pyyntimittaa.")
    print("")
    luokka = input("Anna hyttiluokka (LUX, A, B, C): ").strip().upper()

    if luokka == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
    elif luokka == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif luokka == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif luokka == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print("Virheellinen hyttiluokka.")
        print("")
        sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").strip().lower()
        hb = int(input("Anna hemoglobiiniarvo (g/l): "))

        if sukupuoli == "nainen":
            if hb < 117:
                print("Hemoglobiini on alhainen.")
            elif hb <= 175:
                print("Hemoglobiini on normaali.")
            else:
                print("Hemoglobiini on korkea.")
        elif sukupuoli == "mies":
            if hb < 134:
                print("Hemoglobiini on alhainen.")
            elif hb <= 195:
                print("Hemoglobiini on normaali.")
            else:
                print("Hemoglobiini on korkea.")
        else:
            print("Virheellinen sukupuoli.")
            print("")
            vuosi = int(input("Anna vuosiluku: "))

            if (vuosi % 400 == 0) or (vuosi % 4 == 0 and vuosi % 100 != 0):
                print("Vuosi on karkausvuosi.")
            else:
                print("Vuosi ei ole karkausvuosi.")
