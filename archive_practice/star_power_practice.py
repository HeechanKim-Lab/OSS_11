"""Star pattern generator module."""
# pylint: disable=invalid-name
a = int(input())

for i in range(a):
    for j in range(a-(i+1)):
        print(' ', end='')

    for k in range(1 + 2*(i)):
        print('*', end='')
    print()
