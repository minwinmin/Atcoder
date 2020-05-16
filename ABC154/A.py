S, T = input().split()
A, B = list(map(int, input().split()))
U = input()
if U == S:
    A = A - 1
    print(A , B)
else:
    B = B - 1
    print(A , B)