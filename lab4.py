#Ex1
def calcul_greutate_ideala():
    print("\n--- CALCUL GREUTATE IDEALĂ (formula Lorentz) ---")
    while True:
        try:
            sex = input("Introduceți sexul (M sau F): ").strip().upper()
            if sex not in ["M", "F"]:
                print("Eroare: Sexul poate fi doar 'M' sau 'F'.")
                continue

            varsta = int(input("Introduceți vârsta (ani): "))
            if varsta <= 20 or varsta >= 120:
                print("Eroare: Vârsta trebuie să fie între 21 și 119 ani.")
                continue

            inaltime = int(input("Introduceți înălțimea (cm): "))
            if inaltime < 150 or inaltime > 220:
                print("Eroare: Înălțimea trebuie să fie între 150 și 220 cm.")
                continue

            greutate_actuala = float(input("Introduceți greutatea actuală (kg): "))
            if greutate_actuala < 45 or greutate_actuala > 300:
                print("Eroare: Greutatea trebuie să fie între 45 și 300 kg.")
                continue

            if sex == "M":
                greutate_ideala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
            else:  # sex == "F"
                greutate_ideala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)

            print(f"\nGreutatea ideală este: {greutate_ideala:.2f} kg")

            diferenta = greutate_actuala - greutate_ideala
            if diferenta > 0:
                print("Recomandare: Ar trebui să slăbiți puțin.")
            else:
                print("Recomandare: Ar trebui să adăugați puțină greutate.")
            break

        except ValueError:
            print("Eroare: Introduceți doar valori numerice valide.")
#Ex2
def calcul_varsta_pisica():
    print("\n--- CALCUL VÂRSTĂ PISICĂ ÎN ANI OMENEȘTI ---")
    raspuns = input("Pisica este mai mică de 1 an? (Da/Nu): ").strip().lower()
    
    if raspuns in ["da", "yes"]:
        varste_mici = {
            1: "6 luni",
            2: "10 luni",
            3: "2 ani",
            4: "5 ani",
            5: "8 ani",
            6: "14 ani",
            7: "15 ani",
            8: "16 ani",
            9: "16 ani",
            10: "17 ani",
            11: "17 ani"
        }

        while True:
            try:
                luni = int(input("Câte luni are pisica ta? (1-11): "))
                if luni < 1 or luni > 11:
                    print("Introduceți un număr valid între 1 și 11.")
                    continue
                print(f"Vârsta pisicii în ani omenești este aproximativ: {varste_mici[luni]}")
                break
            except ValueError:
                print("Introduceți o valoare numerică validă.")
    elif raspuns in ["nu", "no"]:
        while True:
            try:
                ani = int(input("Câți ani are pisica ta? (1-34): "))
                if ani < 1 or ani >= 35:
                    print("Introduceți o valoare între 1 și 34.")
                    continue
                if ani == 1:
                    print("În ani omenești, pisica ta are aproximativ 18 ani.")
                elif ani == 2:
                    print("În ani omenești, pisica ta are aproximativ 25 ani.")
                elif 3 <= ani <= 15:
                    ani_omenesti = 25 + (ani - 2) * 4
                    print(f"În ani omenești, pisica ta are aproximativ {ani_omenesti} ani.")
                else:  # ani >= 16
                    ani_omenesti = 25 + (13 * 4) + (ani - 15) * 3
                    print(f"În ani omenești, pisica ta are aproximativ {ani_omenesti} ani.")
                break
            except ValueError:
                print("Introduceți o valoare numerică validă.")
    else:
        print("Răspuns invalid. Te rog răspunde cu Da/Nu sau Yes/No.")

calcul_greutate_ideala()
calcul_varsta_pisica()
