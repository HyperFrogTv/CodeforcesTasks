n = int(input())
score = []
iterator = 0
wynik = 0
for i in range(n):
    score.append(input())

for i in range(n):
    know = score[i].split(" ")
    for e in range(3):
        wynik = wynik + int(know[e])
    if wynik >= 2:
        iterator += 1
    wynik = 0

print(iterator)
