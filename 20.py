n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        if k == 0 or k == i-1:
            print('*', end='')
        else:
            print(' ', end ='')
    print()