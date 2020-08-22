S = input()

if S.count("RRR") == 1:
    print(3)
elif S.count("RR") == 1:
    print(2)
elif S.count("R") != 0:
    print(1)
else:
    print(0)
