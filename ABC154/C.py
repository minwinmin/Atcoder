N = int(input())
A = list(map(int, input().split()))
if len(A) == len(set(A)):
    print("YES")
else:
    print("NO")


"""
bit全探索っぽい
単にリスト内の重複を調べればよくないか？
"""