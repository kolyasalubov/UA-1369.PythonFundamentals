# Поміняйте значення двох змінних без використання третьої змінної
x = int(input('enter a number (x):'))
y = int(input('enter a number (y):'))
x,y = y,x
print('x =', x, '\ny =', y)