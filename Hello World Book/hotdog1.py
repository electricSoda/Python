#this should be done in a virtual machine with a older version of python
#all the "possible combinations" of the hotdog

dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print('\t   Dog \tBun \tKetchup\tMustard\tOnions\tCalories')
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (dog * dog_cal) + (bun * bun_cal) + \
                                (ketchup * ket_cal) + (mustard * mus_cal) + \
                                (onion * onion_cal)
                    print('#', count, '\t', end='')
                    print(dog, '\t', bun, '\t', '\t', ketchup, '\t', end='')
                    print('\t', mustard, '\t', '\t', onion, end = '')
                    print('\t' * 2, total_cal)
                    count = count + 1
