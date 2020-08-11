number_of_times = int(input())
x = 0
for i in range(number_of_times):
    statement = input()
    if statement[0] =="+" and statement[1] =="+" or statement[1] =="+" and statement[2] =="+" or statement[0] =="+" and statement[2] =="+":
        x+=1
    elif statement[0] =="-" and statement[1] =="-" or statement[1] =="-" and statement[2] =="-" or statement[0] =="-" and statement[2] =="-":
        x-=1

print(x)
