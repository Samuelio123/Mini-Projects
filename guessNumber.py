import random

print("	NUMBER GUESSING GAME.")
print("\nI am thinking of a Number between 1 to 20")
num = random.randint(1, 20)

for times in range(1, 6):
#    num = random.randint(1, 20)
    print("Take your guess")
    userGuess = int(input('--> '))

    if userGuess < num:
        print("\nYour guess is low")
    elif userGuess > num:
        print("\nYour guess is high")
    else:
        break

if userGuess == num:
    print("\nGood job! You guessed my Number " + str(times) + ' times')
else:
    print("\nNope. The Number I was thinking of was " + str(num))

