def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print (f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp=bedrag/personen
    return f"Het bedfrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit=[]
    uit.append(tekst)
    uit.append(len(tekst)* "=")
    return uit

def som(mijn_dictionary):
    totaal=0
    for k, v in mijn_dictionary.items():
        totaal += v
    return totaal



     
        

    

     




    