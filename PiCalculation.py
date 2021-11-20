import math

out = 0
for i in range(int(input('Enter amount of runs: '))):
    out += (-1)**i/(2*i+1)
    print('PI is approximately:', out*4)

print(math.pi)
