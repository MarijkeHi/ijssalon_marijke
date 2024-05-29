from helper import som

mijn_dict ={
    "vis": 10,
    "vlees": 25,
    "overig":15
}

totaal=50

def presenteer(dictionary, totaal):
    totaal=som(dictionary)
    for k, v in dictionary.items():
        print (f"{k} : {v} euro")
    print("=========================")
    print(f"totaal : {totaal} euro")

#presenteer(mijn_dict, totaal)
