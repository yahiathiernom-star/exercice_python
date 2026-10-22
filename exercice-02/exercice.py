
def classe_temp(temp):
    if temp < 0:
        print("gel")
    elif temp < 15:
        print("froid")
    elif temp < 25:
        print("doux")    
    else:
        print("chaud")

classe_temp(-3)
classe_temp(0)
classe_temp(15)
classe_temp(31)
print("------------------------------------------------------------------")
def annee_bissextile(annee):
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        print("L'année", annee, "bissextile")
    else:
        print("L'année", annee, "non bissextile")

annee_bissextile(2024)
annee_bissextile(1900)
annee_bissextile(2000)