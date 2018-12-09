n=int(input('enter your number:'))
s = n
for i in range(n):
    for j in range(n):
    	if j == 0:
            print('*' , end='')
    for k in range(i):
	    if k == i-1:
	        print('*', end='')
	    else:
	    	print(' ', end='')
    print()
for i in range(n):
    for j in range(s):
        if j == 0 or j == s-1:
            print('*', end='')
        else:
            print(' ', end='')
    s = s-1
    print()
s = n
for i in range(n):
    for j in range(n):
    	if j == 0:
            print('*' , end='')
    for k in range(i):
	    if k == i-1:
	        print('*', end='')
	    else:
	    	print(' ', end='')
    print()
for i in range(n):
    for j in range(s):
        if j == 0 or j == s-1:
            print('*', end='')
        else:
            print(' ', end='')
    s = s-1
    print()

