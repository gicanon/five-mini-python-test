def item_count_from_index():
    """Accpeting two inputs, a list and an integer-index
    Return a count (number) of how many times the item at that index appears in the list
    Return a empty string ("") if integer-index is out of bounds"""

    input_elements = (input("Enter elements of a list separated by space: "))
    user_list = input_elements.split()
    try:
        input_index = int(input("Enter a number as list index to count how many times the items at that index appears: "))
        return user_list.count(user_list[input_index])
    except (ValueError, IndexError):
        return '""'

print(item_count_from_index())
    
