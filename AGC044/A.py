"""
最初は0なのでD枚支払って、　xを1必ず増やす
Dは絶対に必要な枚数
最小の枚数が必要なので、少ない枚数で実現できるかを考えること

考え方の参考
https://wakabame.hatenablog.com/entry/2020/05/24/031143

"""


"""
T = int(input())
ans = []
for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
"""

T = int(input())
 
for t in range(T):
    N, A, B, C, D = map(int, input().split())
    memo = {}
 
    def dist(n):
        if n == 0:
            return 0
        if n == 1:
            return D
        if n in memo:
            return memo[n]
        #再帰関数になっている
        #確かに求まりそうな感じだ
        ret = min(
            D * n,
            D * abs(n - n//5*5) + C + dist(n//5),
            D * abs(n - (n+4)//5*5) + C + dist((n+4)//5),
            D * abs(n - n//3*3) + B + dist(n//3),
            D * abs(n - (n+2)//3*3) + B + dist((n+2)//3),
            D * abs(n - n//2*2) + A + dist(n//2),
            D * abs(n - (n+1)//2*2) + A + dist((n+1)//2)
        )
 
        memo[n] = ret
        return ret
    print(dist(N))