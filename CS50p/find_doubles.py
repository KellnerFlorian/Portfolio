#define a function that searches a list for doubles
# and prints out the cosisponding element and how often it is in the list
def check_for_doubles(this_list):
    # empty set to save all already seen doubles
    saved_doubles = set()

    for element in this_list:
        if (count(element,this_list) > 1) and (element not in saved_doubles):
            print(f"The element {element} is {count(element,this_list)} times in the list.")
            saved_doubles.add(element)

# define a function that only counts how often an element is in a given list
def count(this_element,that_list):
    counter = 0
    for element in that_list:
        if this_element == element:
            counter = counter + 1
    return counter


# here is a list, that maybe has some doubles in it
list = (1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 10, 10, 10, 10, 10, 10)

check_for_doubles(list)
