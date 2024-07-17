def main():

    # ask the user for a list of numbers and splitting the returning string in seperate numbers
    users_list = input("Please give me some numbers, seperated with spacebar, I will search for the maximum value in your list. ").split()
    users_list = int(users_number) for users_number in users_list

    # search in users list for the maximum value
    answer = MaxFromList(users_list)

    # print the maximum from users list
    print("The number", answer, "is the maximum value of your list.")


# function that finds the maximum value in a list
def MaxFromList(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number

    return max

main()
