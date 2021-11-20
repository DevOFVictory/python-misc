"""
This script prints a diamaond, that opens at the given alphabet letter.
My inspiration for that was the german documentation you can find under this link.
https://youtu.be/V9yPR6WPXZY?t=399 (06:39)

The programmer didnt get it to work.
"""

import string
alph = string.ascii_uppercase

letter = input('Enter a uppercase letter: ')

if letter not in alph:
    print(letter + ' is not in Uppercase ASCII Alphabeth')
    exit(0)

pos = alph.find(letter)+1

lengh = pos*2-1

lines = []

for i in range(1, pos+1):

    line = '-'*(pos-i)

    line += alph[i-1]

    interspace = '-'*(lengh-len(line)*2)

    line += interspace

    if len(interspace) > 0:
        line += alph[i-1]

    line += '-'*(pos-i)

    lines.append(line)

print('\n'.join(lines))
print('\n'.join(lines[::-1][1:]))
