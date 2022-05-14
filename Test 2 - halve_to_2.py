def halve_to_2():
    """Accepting one numeric as input
    Return -1 if number <= 0, if number > 0 divide number by 2 over and over until number < 2
    Return number that is smaller than 2"""

    n1 = int(input("Enter a number: "))
    if n1 <= 0:
        return -1
    else:
        while n1 >= 2:
            n1 = n1 / 2
        return n1

print(halve_to_2())