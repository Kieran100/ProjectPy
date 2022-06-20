while (True):
    year = int(input("Entrez une année :"))
    if (year%4 == 0) and (year%100 != 0):
        print("C'est une année bisextile")
    elif (year%400 == 0):
        print("C'est une année bisextile")
    else :
        print("Ce n'est pas une année bisextile")
