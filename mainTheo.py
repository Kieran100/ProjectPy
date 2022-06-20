
while (True):
    year = int(input("Entre l'année :"))
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("L'année est bisextile")
    else:print("L'année n'est pas bisextile")