def to_jaden_case(string):
    """
    parameter: string
    return: string in UpperCase first letter
    Used join on list comprehension where the string is 
    splitted into words
    """
    return " ".join([s.capitalize() for s in string.split()] )

#print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
    

