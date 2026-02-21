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

