#
# Automaticly color your valorant chat text input
# I recommend to bind this script to a button on your mouse or keyboard using a simple macro application.
#

# Red: <enemy>Text</>
# Blue: <team>Text</>
# Yellow: <system>Text</>
# Green: <notification>Text</>
# Pink: <warning>Text</>

from time import time
from pynput.keyboard import Key, Controller
import pyperclip
import random
import time
keyboard = Controller()

keyboard.press(Key.ctrl)
keyboard.press('a')
keyboard.release('a')
keyboard.release(Key.ctrl)

keyboard.press(Key.ctrl)
keyboard.press('x')
keyboard.release('x')
keyboard.release(Key.ctrl)

latest = ''
colors = ['<enemy>', '<system>', '<notification>', '<team>', '<warning>']
output = ''


mode = 'rainbow'

s = pyperclip.paste()

if mode == 'random':
    for i in s:
        if i != ' ':
            rand = random.choice(colors)
            while rand == latest:
                rand = random.choice(colors)    
            latest = rand
            output += rand + i + '</>'
        else:
            output += ' '

elif mode == 'rainbow':
    counter = 0
    for i in s:
        if i != ' ':
            output += colors[counter % len(colors)] + i + '</>'
            counter += 1
        else:
            output += ' '


pyperclip.copy(output)
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release('v')
keyboard.release(Key.ctrl)

keyboard.press(Key.enter)
keyboard.release(Key.enter)