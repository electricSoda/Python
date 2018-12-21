import time

seconds = int(input('''Countdown Timer:
How many seconds? '''))

print()

for i in range(0, seconds):
    print(seconds, end='')
    for x in range(0, 1):
        print(' * ' * seconds)
    seconds = seconds - 1
    time.sleep(1)

print('BLAST OFF!!!')