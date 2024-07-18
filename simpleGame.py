import random

name = input(print("What is your name?"))

secretNumber = random.randint(1, 10)
print("Choice number between 1 and 10.")
userNumber = int(input("Enter a number: "))
if userNumber == secretNumber:
    print("You win!")
else:
    print("You lose! The secret number is: " + str(secretNumber - userNumber))
