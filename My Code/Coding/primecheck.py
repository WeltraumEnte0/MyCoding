#P R I M E N U M B E R - C H E C K

#number = int(input("Please enter a number "))
number = 3


def check(number):
    result = False
    for factor in range(2, number):
        if number%factor == 0:
            result = False
            break

        else:
            result = True
    if result == True:
        print("It's a prime number")
    else: 
        print("It's not a prime number!")

check(number)