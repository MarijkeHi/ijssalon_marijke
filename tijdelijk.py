from helper import decoreer

def print_aanbieding():
    prijzen={
        "aardbei":3,
        "vanille":4,
        "chocolade":5
    }
    aanbieding=prijzen["aardbei"] * 0.8
    reclame_tekst=(f"Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts E {aanbieding}")
    reclame_tekst2=reclame_tekst[:65]
    reclame_tekst3=reclame_tekst2.upper()
    reclame_tekst4=reclame_tekst3.split(" ")
    el=reclame_tekst2.lower()
    for item in reclame_tekst4:
        if len(item)>=5:
            print (item.upper())
        else:
            print (item.lower())

decoreer("Aanbieding")
print_aanbieding()
