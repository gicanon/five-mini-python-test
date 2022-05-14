def string_expansion():
    """Accepting a non-empty string as input
    Return string that contains every other character 2n+2 times, 
    where n is original index of the letter"""

    my_string = input("Enter a string: ")
    while my_string != "":
        length = len(my_string)
        n = 0
        new_string = ""
        while n < length:
            new_string += (2*n+2)* my_string[n]
            n += 2
        return new_string

print(string_expansion())