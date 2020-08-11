num = int(input())
word = []
for i in range(num):
    word.append(input())

increment = 0
for i in range(num):
    for letter in word[i]:
        increment += 1

    if increment > 10:
        print(word[i][0] + str(increment-2) + word[i][increment-1])
    else:
        print(word[i])
    increment = 0


