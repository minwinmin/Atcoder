N = int(input())
AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(1, N+1):
    S = input()
    if S == "AC":
        AC += 1
    elif S == "WA":
        WA += 1
    elif S == "TLE":
        TLE += 1
    else:
        RE += 1
print("AC x " + str(AC))
print("WA x " + str(WA))
print("TLE x " + str(TLE))
print("RE x " + str(RE))