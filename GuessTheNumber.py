import random
a=random.randint(0,20)

while True:
    b = int(input("Enter random Number \n"))
    if a==b:
        print("Guessed Number is Currect")
    elif a>b:
        print("guess another high Number")
    else:
        print("guess another low Number")

