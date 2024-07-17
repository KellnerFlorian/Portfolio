# startvalues of the fibonacci sequence
f1 = 0
f2 = 1

# ask the user how many fibonacci number should be printed
n = int(input("How many fibonacci numbers should be printed? "))

# empty list
fibonacciList = []

# generate the first n fibonacci numbers
# if the user wants only the first element
if n == 1:
    print(f"This is the first fibonacci number: {f1}")

# if the user wants only the first two elements
elif n == 2:
    print(f"These are the first two fibonacci numbers: {f1}, {f2}")

# if the user wants the first n elements
elif n > 2:
    fibonacciList = [0, 1]
    i = 2
    while i < n:
        fi = fibonacciList[i - 1] + fibonacciList[i - 2]
        fibonacciList.append(fi)
        i = i + 1
    # print all the numbers in a row
    print(f"These are the first {n} fibonacci numbers: ", end="")
    for number in fibonacciList:
        print(number, end = ", ")
