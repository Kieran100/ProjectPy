annee = int(input("Entrez l annee a verifier:"))
if(annee%4==0 and annee%100!=0 or annee%400==0):
    print("L'annee est une annee bissextile!")
else:
    print("L'annee n'est pas une annee bissextile!")