import easygui, random


seceret = random.randint(1,100)
guess = 0
tries = 0


easygui.msgbox('''AHOY!
I'm the Dread Pirate Roberts, and I have a seceret!
It is a number between 1 to 99.
I'll give you 6 tries.''', title = 'Number Guess Game', ok_button = 'Next')

while guess != seceret and tries < 8:
    guess = easygui.integerbox("What's yer guess, matey?")
    if not guess: break
    if guess < seceret:
        easygui.msgbox(str(guess) + ' is too low, ye scurvy dog!', title = 'Too Low!', ok_button = 'Continue')
    elif guess > seceret:
        easygui.msgbox(str(guess) + ' is too high, landlubber!', title = 'Too High!', ok_button = 'Continue')
    tries = tries + 1

if guess == seceret:
    easygui.msgbox('Avast! Ye got it! Found my seceret, ye did!', title = 'Winner!', ok_button = 'Exit')
else:
    easygui.msg('No more guesses! Better luck next time, matey!', title = 'Try again!', ok_button = 'OK') 
