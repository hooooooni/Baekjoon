import sys
input = sys.stdin.readline

a = int(input())
b = int(a/4)
y = ''

for i in range(b):
    y = y+'long '

print(y+'int')