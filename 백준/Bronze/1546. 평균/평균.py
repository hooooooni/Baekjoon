import sys
input = sys.stdin.readline

a = int(input())
lst = list(map(int,input().split()))

b = max(lst)

for i in range(a) :
    lst[i] = lst[i]/b*100


avg = sum(lst)/a
print(avg)