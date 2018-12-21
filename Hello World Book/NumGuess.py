import random
import time

seceret = random.randint(1,100)
guess = 0
tries = 0

print('AHOY! I\'m the Dread Pirate Roberts, and I have a seceret!')
print('It is a number frome 1 to 99. I\'ll give you 6 tries. ')

while guess != seceret and tries < 10:
    guess = int(input('What\'s yer guess? '))
    if guess < seceret:
        print('Too low, ye scurvy dog!')
    elif guess > seceret:
        print('Too high, landlubber!')
    tries = tries + 1

if guess == seceret:
    print('Avast! Ye got it! Found my seceret, ye did!')
else:
    print('No more guesses! Better luck next time matey!')
    print('Me seceret was ' + str(seceret))
