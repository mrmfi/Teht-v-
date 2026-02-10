import math
import random

# ----------------------------
# 2. Muuttujat ja vuorovaikutteiset ohjelmat
# ----------------------------

# 1) Nimi ja tervehdys
name = input("Anna nimesi: ")
print(f"Terve, {name}!\n")

# 2) Ympyrän pinta-ala
r = float(input("Anna ympyrän säde: "))
area = math.pi * r * r
print(f"Ympyrän pinta-ala on {area:.2f}\n")

# 3) Suorakulmion piiri ja pinta-ala
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus
print(f"Suorakulmion piiri on {piiri:.2f}")
print(f"Suorakulmion pinta-ala on {pinta_ala:.2f}\n")

# 4) Kolme kokonaislukua: summa, tulo, keskiarvo
a = int(input("Anna 1. kokonaisluku: "))
b = int(input("Anna 2. kokonaisluku: "))
c = int(input("Anna 3. kokonaisluku: "))
summa = a + b + c
tulo = a * b * c
keskiarvo = summa / 3
print(f"Summa: {summa}")
print(f"Tulo: {tulo}")
print(f"Keskiarvo: {keskiarvo:.2f}\n")

# 5) Leiviskät, naulat, luodit -> kilogrammat ja grammat
leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))

total_luoti = (leiviska * 20 * 32) + (naula * 32) + luoti
total_grams = total_luoti * 13.3

kg = int(total_grams // 1000)
g = total_grams - kg * 1000
print(f"Massa on {kg} kg ja {g:.1f} g (yhteensä {total_grams:.1f} g)\n")

# ----------------------------
# 6. Random-koodit
# ----------------------------

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
print()

# ----------------------------
# 3. Valintarakenne (if)
# ----------------------------

# 3.1) Kuha
pituus = int(input("Anna kuhan pituus (cm): "))
minimi = 37

if pituus < minimi:
    puuttuu = minimi - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Puuttuu {puuttuu} cm.\n")
else:
    print("Kuha on sallittua pyyntimittaa.\n")

# 3.2) Hyttiluokka
luokka = input("Anna hyttiluokka (LUX, A, B, C): ").strip().upper()

if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.\n")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.\n")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.\n")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.\n")
else:
    print("Virheellinen hyttiluokka.\n")

# 3.3) Hemoglobiini
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").strip().lower()
hb = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiini on alhainen.\n")
    elif hb <= 175:
        print("Hemoglobiini on normaali.\n")
    else:
        print("Hemoglobiini on korkea.\n")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiini on alhainen.\n")
    elif hb <= 195:
        print("Hemoglobiini on normaali.\n")
    else:
        print("Hemoglobiini on korkea.\n")
else:
    print("Virheellinen sukupuoli.\n")

# 3.4) Karkausvuosi
vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 400 == 0) or (vuosi % 4 == 0 and vuosi % 100 != 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
