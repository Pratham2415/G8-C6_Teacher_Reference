number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))
number_3 = int(input("Enter the third number : "))

if number_1 > number_2 and number_1 > number_3:
    print("Number 1 is the largest")
elif number_2 > number_3 and number_2 > number_1:
    print("Number 2 is the largest")
else:
    print("Number 3 is the largest")
