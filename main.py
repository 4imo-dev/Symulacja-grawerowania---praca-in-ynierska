import turtle
from literki import litery

# Słownik przypisujący znak do odpowiedniej funkcji rysującej
ALFABET = {
    'A': litery.litera_A, 'B': litery.litera_B, 'C': litery.litera_C, 'D': litery.litera_D, 'E': litery.litera_E,
    'F': litery.litera_F, 'G': litery.litera_G, 'H': litery.litera_H, 'I': litery.litera_I, 'J': litery.litera_J,
    'K': litery.litera_K, 'L': litery.litera_L, 'M': litery.litera_M, 'N': litery.litera_N, 'O': litery.litera_O,
    'P': litery.litera_P, 'R': litery.litera_R, 'S': litery.litera_S, 'T': litery.litera_T, 'U': litery.litera_U, 
    'W': litery.litera_W, 'Y': litery.litera_Y, 'Z': litery.litera_Z
}

# Wyznaczone szerokości dla każdej litery osobno proporcjonalnie do skali
SZEROKOSCI_LITER = {
    'A': 0.8, 'B': 0.65, 'C': 0.7, 'D': 0.7, 'E': 0.5,
    'F': 0.5, 'G': 0.7, 'H': 0.6, 'I': 0, 'J': 0.25,
    'K': 0.5, 'L': 0.45, 'M': 1.0, 'N': 0.7, 'O': 0.8,
    'P': 0.5, 'R': 0.5, 'S': 0.5, 'T': 0.7, 'U': 0.7,
    'W': 1.2, 'Y': 0.6, 'Z': 0.6,
}

# ==============================================================================
# GŁÓWNY PROGRAM
# ==============================================================================

def wykonaj_grawerowanie():
    # === POBIERANIE DANYCH OD UŻYTKOWNIKA ===
    tekst = input("Wpisz tekst do wygrawerowania (duże litery, bez polskich znaków): ").upper()
    skala = float(input("Podaj wielkość czcionki (np. 100): "))
    szerokosc_kartki = float(input("Podaj szerokość obszaru roboczego (np. 1000): "))
    wysokosc_kartki = float(input("Podaj wysokość obszaru roboczego (np. 700): "))

    m_gorny = float(input("Podaj wielkość marginesu górnego: "))
    m_dolny = float(input("Podaj wielkość marginesu dolnego: "))
    m_lewy = float(input("Podaj wielkość marginesu lewego: "))
    m_prawy = float(input("Podaj wielkość marginesu prawego: "))

    wyr_pionowe = input("Wyrównanie w pionie (GORA / SRODEK / DOL): ").strip().upper()
    wyr_poziome = input("Wyrównanie w poziomie (LEWO / SRODEK / PRAWO): ").strip().upper()

    # === OBLICZANIE OBSZARU UŻYTKOWEGO W ZAWIERANIE MARGINESÓW ===
    dostepna_szerokosc = szerokosc_kartki - (m_lewy + m_prawy)
    dostepna_wysokosc = wysokosc_kartki - (m_gorny + m_dolny)

    if dostepna_szerokosc <= 0 or dostepna_wysokosc <= 0:
        print("\n[BŁĄD]: Marginesy są zbyt duże! Brak wolnego miejsca na kartce.")
        return

    # Granice obszaru użytkowego
    obszar_min_x = -szerokosc_kartki / 2 + m_lewy
    obszar_max_x = szerokosc_kartki / 2 - m_prawy
    obszar_max_y = wysokosc_kartki / 2 - m_gorny
    obszar_min_y = -wysokosc_kartki / 2 + m_dolny



    # === PARAMETRY WYKORZYSTYWANE DO OBLICZEŃ POSZCZEGÓLNYCH LITER ===
    szerokosc_znakow = {znak: skala * szerokosc for znak, szerokosc in SZEROKOSCI_LITER.items()}  # Inna szerokość dla każdego znaku
    odstep_znakow = skala * 0.2    # Odstęp między literami
    odstep_linii = skala * 1.5     # Odstęp między liniami tekstu
    szerokosc_spacji = skala * 0.5 # Szerokość spacji

    slowa = tekst.split()

    # === SPRAWDZANIE CZY TEKST ZMIEŚCI SIĘ NA PODANEJ KARTCE ===
    linie = []
    aktualna_linia = []
    szerokosc_aktualnej_linii = 0

    for slowo in slowa:
        # === SPRAWDZANIE CZY SŁOWO ZAWIERA TYLKO DOZWOLONE ZNAKI ===
        for znak in slowo:
            if znak not in ALFABET:
                print(f"\n[BŁĄD]: Niepoprawny znak '{znak}' w słowie '{slowo}'. Dozwolone są tylko duże litery A-Z.")
                return
        
        # === OBLICZANIE SZEROKOŚCI SŁOWA ===
        szerokosc_slowa = sum(szerokosc_znakow[znak] + odstep_znakow for znak in slowo)

        if slowo:
            szerokosc_slowa += (len(slowo) - 1) * odstep_znakow  # Usuwanie ostatniego odstępu po literze

        dodatek_spacji = szerokosc_spacji if aktualna_linia else 0

        if szerokosc_aktualnej_linii + dodatek_spacji + szerokosc_slowa <= dostepna_szerokosc:
            aktualna_linia.append(slowo)
            szerokosc_aktualnej_linii += dodatek_spacji + szerokosc_slowa
        else:
            if szerokosc_slowa > dostepna_szerokosc:
                print("\n[BŁĄD]: Pojedyncze słowo jest zbyt szerokie na podany wymiar obszaru roboczego!")
                return
            linie.append(aktualna_linia)
            aktualna_linia = [slowo]
            szerokosc_aktualnej_linii = szerokosc_slowa

    if aktualna_linia:
        linie.append(aktualna_linia)

    # === SPRAWDZANIE CZY TEKST ZMIEŚCI SIĘ W PIONIE NA PODANEJ KARTCE ===
    liczba_linii = len(linie)
    calkowita_wysokosc_tekstu = (liczba_linii -1) * odstep_linii + skala
    if calkowita_wysokosc_tekstu > dostepna_wysokosc:
        print("\n[BŁĄD]: Tekst jest zbyt długi przez co nie zmieści się w pionie na podanym wymiarze obszaru roboczego!")
        return

    # === OBLICZENIE PUNKTU STARTOWEGO DLA POZYCJONOWANIA W PIONIE ===
    if wyr_pionowe == "GORA":
        start_y = obszar_max_y - skala
    elif wyr_pionowe == "DOL":
        start_y = obszar_min_y + (calkowita_wysokosc_tekstu - skala)
    elif wyr_pionowe == "SRODEK":
        srodek_obszaru_y = (obszar_max_y + obszar_min_y) / 2
        start_y = srodek_obszaru_y + (calkowita_wysokosc_tekstu / 2) - skala
    else:  
        print("\n[BŁĄD]: Niepoprawne wyrównanie w pionie! Wybierz GORA, SRODEK lub DOL.")
        return

    # === TURTLE - SYMULACJA GRAWEROWANIA ===
    ekran = turtle.Screen()
    ekran.setup(szerokosc_kartki + 60, wysokosc_kartki + 60)
    ekran.title("Symulacja grawerowania robotem")

    robot = turtle.Turtle()
    robot.speed(0)  # Ustawienie maksymalnej prędkości rysowania
    robot.left(90)  # Ustawienie orientacji robota pionowo w górę

    # === RYSOWANIE RAMKI ===
    # Zewnętrzna krawędź kartki
    robot.penup()
    robot.goto(-szerokosc_kartki / 2, wysokosc_kartki / 2)
    robot.pendown()
    robot.color("black")
    for _ in range(2):
        robot.forward(-wysokosc_kartki)
        robot.left(90)
        robot.forward(-szerokosc_kartki)
        robot.left(90)
    robot.color("red")

    # Wewnętrzny obszar roboczy z uwzględnieniem marginesów
    robot.penup()
    robot.goto(obszar_min_x, obszar_max_y)
    robot.pendown()
    robot.color("pink")
    robot.goto(obszar_max_x, obszar_max_y)
    robot.goto(obszar_max_x, obszar_min_y)
    robot.goto(obszar_min_x, obszar_min_y)
    robot.goto(obszar_min_x, obszar_max_y)
    robot.penup()

    robot.color("black")
    robot.speed(3)

    # === RYSOWANIE TEKSTU ===
    print("\n[INFO]: Tekst się zmieści. Rozpoczynam grawerowanie ...")

    for nr_linii, linia in enumerate(linie):
        # Obliczanie szerokości bieżącej linii
        szerokosc_linii = 0
        for i, slowo in enumerate(linia):
            dlugosc_slowa = sum(szerokosc_znakow[znak] for znak in slowo)
            if slowo:
                dlugosc_slowa += (len(slowo) - 1) * odstep_znakow
            szerokosc_linii += dlugosc_slowa
            if i < len(linia) - 1:
                szerokosc_linii += szerokosc_spacji

    # Wyznaczenie punktu początkowego w poziomie dla danej linii - DO POPRAWY
        if wyr_poziome == "LEWO":
            start_x = obszar_min_x
        elif wyr_poziome == "PRAWO":
            start_x = obszar_max_x - szerokosc_linii
        else:  # SRODEK
            srodek_obszaru_x = (obszar_min_x + obszar_max_x) / 2
            start_x = srodek_obszaru_x - (szerokosc_linii / 2)

        y_linii = start_y - nr_linii * odstep_linii
        robot.penup()
        robot.goto(start_x, y_linii)


    # Rysowanie wyrazów
        for index_slowa, slowo in enumerate(linia):
            for index_litery, litera in enumerate(slowo):
                x_litery, y_litery = robot.position()
                ALFABET[litera](robot, skala)

                robot.penup()
                robot.goto(x_litery + szerokosc_znakow[litera], y_litery)

                # Dodanie odstępu między literami (oprócz ostatniej w słowie)
                if index_litery < len(slowo) - 1:
                    robot.penup()
                    robot.goto(robot.xcor() + odstep_znakow, robot.ycor())

            # Dodanie jednakowej spacji po słowie
            if index_slowa < len(linia) - 1:
                robot.penup()
                robot.goto(robot.xcor() + szerokosc_spacji, robot.ycor())

    print("[INFO]: Grawerowanie zakończone pomyślnie!")
    turtle.done()

# === URUCHOMIENIE PROGRAMU ===
wykonaj_grawerowanie()
