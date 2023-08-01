import sys
input = sys.stdin.readline

word = input().strip()
word = word.upper()

s = list(set(word))
cnt_list = []

for i in s :
    cnt = word.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    x = cnt_list.index(max(cnt_list))
    print(s[x])