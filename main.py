# ošetřit: soubor neexistuje (2), smazání poznámky z prázdného dokumentu (3)

# Knihovny
from time import sleep


# Proměnné
oddelovac = "-"*40
hl_fce = ""
vych_nazev_soub = "Textový dokument.txt"
i = 1
hlavicka = ("Vítej ve správci poznámek".upper().center(40) + f"\n{oddelovac}\n"
+ "Možnosti pro správu poznámek:\n"
+ "    1. Přidat novou poznámku\n"
+ "    2. Zobrazit všechny poznámky\n"
+ "    3. Smazat konkrétní poznámku\n"
+ "    4. Ukončit program\n" + oddelovac)


# Vlastní aplikace
print(hlavicka)
while True:
    # Smyčka pro nesprávné znaky
    if hl_fce not in ["1", "2", "3", "4"]:
        if hl_fce != "":
            hl_fce = input("Zadej číslo od 1 do 4\n")
            continue
        else: hl_fce = input("Zadej funkci (1 - 4) a potvrď klávesou Enter: ")
    
    # Nová poznámka
    if hl_fce == "1":
        text = input("Napiš novou poznámku:\n")
        with open(vych_nazev_soub, "a") as doc:
            doc.write(text + "\n")
        dalsi_pozn = input("Chceš zapsat další? (y/n)\n")
        while dalsi_pozn not in ["y", "n"]:
            dalsi_pozn = input("Chceš zapsat další? (y/n)\n")
        else:
            if dalsi_pozn == "y":
                hl_fce = "1"
                continue
            else:
                hl_fce = ""
                print("\n" + hlavicka)
                continue

    # Zobratit poznámky
    if hl_fce == "2":
        obsah = []
        try:
            with open(vych_nazev_soub, "r") as doc:  # načtení obsahu souboru od listu
                for row in doc:
                    obsah.append(row.strip())
            while '' in obsah:  # očištění listu od prázdných řádků
                obsah.remove('')
            if obsah == []: # ošetření prázdného dokumentu
                print("Dokument je prázdný. Budeš přesměrován na úvod.")
                hl_fce = ""
                sleep(2)
                print("\n" + hlavicka)
                continue
            with open(vych_nazev_soub, "r") as doc:  # vypsání poznámek
                print("Zapsané poznámky:")
                for i, row in enumerate(doc, 1):
                    print(f"{i}. {row.strip()}")
        except FileNotFoundError:   # ošetření chybějícího souboru
            print("Zatím jsi žádný dokument nevytvořil. Budeš přesměrován na úvod.")
            hl_fce = ""
            sleep(2)
            print("\n" + hlavicka)
            continue
        hl_fce = ""
        input("Stiskni enter pro návrat do nabídky\n")
        print(hlavicka)
    
    # Odebrat poznámku
    if hl_fce == "3":
        obsah = []
        try:
            with open(vych_nazev_soub) as doc:  # načtení obsahu souboru od listu
                for row in doc:
                    obsah.append(row.strip())
        except FileNotFoundError:   # ošetření chybějícího souboru
            print("Zatím jsi žádný dokument nevytvořil. Budeš přesměrován na úvod.")
            hl_fce = ""
            sleep(2)
            print("\n" + hlavicka)
            continue
        while '' in obsah:  # očištění listu od prázdných řádků
            obsah.remove('')
        if obsah == []: # ošetření prázdného dokumentu
            print("Dokument je prázdný. Budeš přesměrován na úvod.")
            hl_fce = ""
            sleep(2)
            print("\n" + hlavicka)
            continue
        odstr_pozn = input("Zadej číslo poznámky, kterou chceš odstranit: ")    # Výběr poznámky k odstranění
        while odstr_pozn.isdigit() is False or (int(odstr_pozn) - 1) not in range(len(obsah)):
            odstr_pozn = input("Je třeba zadat číslo odpovídající existující poznámce: ")
        del obsah[int(odstr_pozn) - 1]    # odstranění poznámky
        open(vych_nazev_soub, "w").close()  # smazání obsahu původního souboru
        with open(vych_nazev_soub, "a") as doc: # zapsání nového obsahu
            for row in obsah:
                doc.write(row + "\n")
            else: print("\nÚspěšně odstraněno. Budeš přesměrován na úvod.\n"
                        + "Chceš-li odstranit další, prohlédni si nejdříve nové pořadí poznámek.")    # kontrola úspěchu vymazání
        hl_fce = ""
        sleep(3)
        print("\n" + hlavicka)

    # Ukončit
    if hl_fce == "4":
        print("Ukončuji aplikaci...")
        sleep(2)
        exit()