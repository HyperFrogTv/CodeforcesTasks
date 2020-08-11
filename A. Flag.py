a = input().split(" ")
n = int(a[0])
m = int(a[1])
i = 1
flag = 0
rows = []
while i <= n:
    rows.append(input())
    i += 1

for w in range(n):
    for e in range(m-1):
        if rows[w][e] != rows[w][e+1]:
            flag = 1


for w in range(n-1):
    for e in range(m):
        if rows[w][e] == rows[w+1][e]:
            flag = 1
if flag == 0:
    print('Yes')
else:
    print('No')
