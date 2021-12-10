import random
# schrijven waarmee je een zak met M&M’s kan vullen.

# Maak een List waar de volgende kleuren in zitten: oranje, blauw, groen, bruin
# Maak een functie die een List datatype (zak met M&M’s) aanmaakt en vult met kleuren
# De functie heeft 1 parameter → een int met het aantal M&M’s (die een random kleur krijgen) en die dan aan de zak worden toegevoegd
# De functie voegt willekeurige een kleur (M&M) toe aan de zak. De beschikbare kleuren staan in de List aangemaakt in punt 1
# De functie geeft de List (zak met M&M’s) terug als return value
# Het programma vraagt met een input hoeveel kleuren (M&M’s) er aan de zak toegevoegd moeten worden
# Het programma print als laatste de inhoud uit van de zak met M&M’s
aantalMenM = int(input('Hoeveel MenM wilt u in de zak? '))
mnmDictionaryBag = {
  'oranje': 0,
  'rood' : 0,
  'geel' : 0,
  'bruin' : 0
}

# MenMkleurendictionary = {'Kleuren':['Oranje', 'Blauw', 'Groen', 'Bruin']}
MenMKleuren = ['oranje','rood','geel','bruin']
# MenMzak = []


# def GenerateMenM(aantalMenM):
#     for x in range(aantalMenM):
#         Kleurnummer = random.randint(0,3)
#         MenMzak.append(MenMkleuren[Kleurnummer])
        
#     print(MenMzak)
#     return MenMzak
# MenM = GenerateMenM(aantalMenM)
# print(mnmDictionaryBag)

def MenMdictionary(aantalMenM,mnmDictionaryBag):
    for x in range(aantalMenM):
        kleurMM = random.choice(MenMKleuren)
        mnmDictionaryBag[kleurMM] += 1
    return mnmDictionaryBag
    

mnmDictionaryBag = MenMdictionary(aantalMenM,mnmDictionaryBag)
print(mnmDictionaryBag)
