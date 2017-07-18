a = [1, 'event', 'project', 6]
b = ['', '']

b[0] = a[1]
b[1] = a[2] + ' ' + str(a[3])

print(b)
