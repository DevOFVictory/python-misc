#
# VERY simple one-line password generator
#

import random,string,pyperclip
pyperclip.copy(''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~') for _ in range(random.randint(20, 35))))
