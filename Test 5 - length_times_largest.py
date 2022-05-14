def length_times_largest():
    """Accepting a list as input
    Return length of list * largest integer (not float) in the list
    Return empty list ("") if list does not contain an integer"""

    input_elements = (input("Enter elements of a list separated by space: "))
    user_list = input_elements.split()
    integer_list = []
    length = len(user_list)
    i = 0
    while i < length:
        try: 
            integer_list.append(int(user_list[i]))
            i += 1
        except ValueError:
            i += 1
    if integer_list:
        return length * max(integer_list)
    else:
        return '""'

print(length_times_largest())