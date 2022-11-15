formetexte = int(input("Bonjours, si vous voulez entrer un texte veulliez taper 1, si vous voulez joindre un fichier taper 2: "))
confirmation1 = 0
def premierinterface(a):
    if a == 1:
        confirmation1 = 1
        texte = str(input("Veulliez rentrer le texte: "))
    elif a ==2:
        confirmation1 = 1
    else:
        print("erreur, veuiller taper 1 si vous voulez entrer un texte, si vous voulez joindre un fichier taper 2")
premierinterface(formetexte)
if a == 0