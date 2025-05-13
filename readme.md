# 🗂️ Správce poznámek (Terminálová aplikace v Pythonu)

**Autor:** rich95cz  
**Verze:** 1.0  
**Jazyk:** Python 3.13.3  
**Knihovny:** `time`

## 🧠 O projektu

Tato jednoduchá aplikace pro příkazovou řádku umožňuje správu poznámek.  
Uživatel může poznámky přidávat, prohlížet, mazat a vše se ukládá do textového souboru.

Projekt byl vytvořen v rámci samostudia pro procvičení práce s podmínkami, cykly, vstupem od uživatele, se soubory a základy funkcí v Pythonu.

## 🛠️ Funkcionalita

- ✅ Přidání nové poznámky
- ✅ Výpis všech uložených poznámek (s očíslováním)
- ✅ Odstranění poznámky podle jejího čísla
- ✅ Trvalé uložení poznámek do `.txt` souboru
- ✅ Ošetření chyb – např. chybějící soubor nebo prázdný soubor
- ✅ Přívětivý výpis a interaktivní menu

## 📂 Soubory v projektu

- `main.py` – hlavní skript s kódem aplikace
- `Textový dokument.txt` – generovaný soubor pro ukládání poznámek (vytvoří se automaticky)

## ▶️ Jak spustit program

Otevři terminál v adresáři se souborem a spusť:

```bash
python main.py
```

## ✨ Ukázka práce

```----------------------------------------
        VÍTEJ VE SPRÁVCI POZNÁMEK        
----------------------------------------
Možnosti pro správu poznámek:
    1. Přidat novou poznámku
    2. Zobrazit všechny poznámky
    3. Smazat konkrétní poznámku
    4. Ukončit program
----------------------------------------
```



## ✅ Dovednosti, které projekt ukazuje

- Práce s textovými soubory (čtení, zápis, mazání obsahu)

- Základy cyklů (while, for) a podmínek

- Uživatelské vstupy a validace

- Struktura programu pomocí funkcí (základní úroveň)

- Přehledná interakce v konzoli

## 💡 Možnosti rozšíření

- Třídění poznámek podle času nebo abecedy

- Ukládání s časovou značkou

- Hledání poznámky podle klíčového slova

- Barevné výpisy pomocí colorama

- Refaktoring pomocí vlastních funkcí