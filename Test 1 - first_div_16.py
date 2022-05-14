def first_div_16():
    """Accepting two positive integers, n1 and n2 as inputs 
    Return the first number in range(n1,n2) that is divisible by 16
    Return 0 if non of the number is divisible by 16"""

    n1 = int(input("Enter an positive integer for n1: "))
    n2 = int(input("Enter an positive integer for n2: "))
    
    while n1 and n2 > 0:
        for num in range(n1,n2):
            if num % 16 == 0:
                return num
        return 0

print(first_div_16())

   