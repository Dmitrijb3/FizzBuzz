fzbz = input("Select a number between 1 and 100: ")
fzbz = int(fzbz)
for value in range(1, fzbz+1):
    if value % 3 == 0 and value % 5 == 0:
        print("fizzbuzz")
    elif value % 3 == 0:
        print("fizz")
    elif value % 5 == 0:
        print("buzz")
    else:
        print(value)
