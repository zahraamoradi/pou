n = int(input('enter your number:'))
s = n
for i in range(n):
    for j in range(s):
        if j == 0 or j == s-1:
            print('*', end='')
        else:
            print(' ', end='')
    s = s-1
    print()
