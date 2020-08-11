value = input()

score_value = input()


nk = value.split(" ")

score = score_value.split(" ")

n = int(nk[0])
k = int(nk[1])
iterator = 0
i = 0
while i < n:
    if (int(score[i]) >= int(score[k-1])) and int(score[i]) != 0:
        iterator += 1
    i = i + 1
print(iterator)

