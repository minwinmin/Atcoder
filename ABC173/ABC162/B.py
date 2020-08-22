N = int(input())
summ = 0
for i in range(1, N+1):
    if (i%15 != 0) and (i%3 != 0) and (i%5 != 0):
        summ = summ + i
print(summ)