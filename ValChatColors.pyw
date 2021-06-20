# Red: <enemy>Text</>
# Blue: <team>Text</>
# Yellow: <system>Text</>
# Green: <notification>Text</>
# Pink: <warning>Text</>

from pynput.keyboard import Key, Controller
import pyperclip
import random
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
colors = ['<enemys>', '<team>', '<system>', '<notification>', '<warning>']
output = ''
s = pyperclip.paste()


for i in s:
    rand = random.choice(colors)
    while rand == latest:
        rand = random.choice(colors)
    latest = rand
    output += rand + i + '</>'


pyperclip.copy(output)
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release('v')
keyboard.release(Key.ctrl)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
