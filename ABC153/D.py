H = int(input())
c = 1
tf = True
while tf:
    if H//2 >= 1:
        c += 1
        H = H//2
    else:
        tf = False
print(2**c-1)
