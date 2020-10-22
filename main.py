from random import randint

number = randint(0, 100)

while True:
    user = int(input("Enter an integer between 0 and 100: "))
    if user < number:
        print("number is higher")
    elif user > number:
        print("number is lower")
    elif user == number:
        print(f"You win! the number was: {number}")
        break
