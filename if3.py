#!/usr/bin/python3

# puzzle number game

number = 7
guess = -1
print("guess number")
while guess != number:
    guess = int(input("input you nubmer:"))

    if guess == number:
     print("congratulation you are right")
    elif guess < number:
     print("your number is small")
    elif guess > number:
     print("your number is big")
