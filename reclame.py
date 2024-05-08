from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs - prijs * korting
    
    uitvoer =f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {korting} euro."
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten):
    totaal=0
    for nr in inkomsten:
        totaal += nr
    bedrag = totaal * 0.09
    
    uitvoer=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden." 
    return uitvoer

print(inkomsten_totaal(inkomsten=[150, 200, 130, 145, 90, 80, 180]))

def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)

print(laag_en_hoog(mijn_lijst=[150, 200, 130, 145, 90, 80, 180]))

def gemiddelde(mijn_lijst):
    total = 0
    for nr in mijn_lijst:
        total= total + nr
    gemiddelde= total/len(mijn_lijst)
    uitvoer=f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro." 
    return uitvoer


print(gemiddelde(mijn_lijst=[150, 200, 130, 145, 90, 80, 180]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
      
print(meervoudig(invoer_lijst=[10, 5, 15, 24, 3, 2, 1, 2, 9]))

def combinatie(invoer_lijst_2):
    korte_lijst=meervoudig(invoer_lijst_2)
    uitvoer=mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
print(combinatie(invoer_lijst_2=[1, 10, 3, 6, 9, 2, 11, 24, 5]))