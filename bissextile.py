''' Fonction pour savoir si l'annee est bissextile qui prends un nombre en entree '''

def func_bissextile(year):
    if year % 4 == 0: # Divisible par 4?
        if year % 100 != 100: # Pas Divisible par 100?
            print("Annee bissextile")
        else:
            print("Annee pas bissextile")
    else: 
        print("Annee pas bissextile")

func_bissextile(1230)