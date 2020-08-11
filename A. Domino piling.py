
input_value = input().split()

m = int(input_value[0])
n = int(input_value[1])
dominos = 0

pom = [[0 for x in range(n)] for y in range(m)]

if n <= 1 and m <= 1:
    dominos = 0
else:
    if n > 1:
        for i in range(m):
            for o in range(n-1):
                if pom[i][o] == 0 and pom[i][o+1] == 0:
                    pom[i][o] = 1
                    pom[i][o+1] = 1
                    dominos += 1

    if m > 1:
        for i in range(m-1):
            for o in range(n):
                if pom[i][o] == 0 and pom[i+1][o] == 0:
                    pom[i][o] = 1
                    pom[i+1][o] = 1
                    dominos += 1

print(dominos)
