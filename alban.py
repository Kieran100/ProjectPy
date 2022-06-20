
def ask_user_input():
    """ return function check_error with a input string"""

    print("Entrez une année:")
    input_year = input()

    if input_year == "":
        return ask_user_input()
    else:
        return check_error(input_year)


def check_error(year):
    """ return year if the input is numeric

    else return function ask_user_input
    """

    if year.isnumeric() == False:
        print("votre année n'est pas numerique")
        return ask_user_input()
    else:
        return year


def check_if_bisextil(year):
    """ return a boolean

     True if the year is bisextile

     False if is not
     """

    year = int(year)

    if year%4 == 0 and year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

def print_result(is_bisextile):
    """ print a text"""

    if is_bisextile == True:
        print("l'année est bisextile !")
    else:
        print("l'année n'est pas bisextile")



input_year = ask_user_input()


is_bisextile = check_if_bisextil(input_year)

print_result(is_bisextile)



