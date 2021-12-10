import random
# schrijven waarmee je een zak met M&M’s kan vullen.

# Maak een List waar de volgende kleuren in zitten: oranje, blauw, groen, bruin
# Maak een functie die een List datatype (zak met M&M’s) aanmaakt en vult met kleuren
# De functie heeft 1 parameter → een int met het aantal M&M’s (die een random kleur krijgen) en die dan aan de zak worden toegevoegd
# De functie voegt willekeurige een kleur (M&M) toe aan de zak. De beschikbare kleuren staan in de List aangemaakt in punt 1
# De functie geeft de List (zak met M&M’s) terug als return value
# Het programma vraagt met een input hoeveel kleuren (M&M’s) er aan de zak toegevoegd moeten worden
# Het programma print als laatste de inhoud uit van de zak met M&M’s


MenMkleuren = ['Oranje', 'Blauw', 'Groen', 'Bruin']

MenMzak = []
aantalMenM = int(input('Hoeveel MenM wilt u in de zak? '))
def GenerateMenM(aantalMenM):
    for x in range(aantalMenM):
        Kleurnummer = random.randint(0,3)
        MenMzak.append(MenMkleuren[Kleurnummer])
        
    print(MenMzak)
    return MenMzak
MenM = GenerateMenM(aantalMenM)




def zakMenM(MenMkleuren):
    pass

