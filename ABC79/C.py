A,B,C,D = map(int, input())

for i in range(2**3):
    f = ["-", "-", "-"]
    for j in range(2*3):
        if((i >> j) & 1):
        
    

"""
A+B+C+D=7
符号が入るのは3箇所。
→この組み合わせは2^N
これを全探索していく。
- : 0
+ : 1 ...フラグ
とする。
まず、["-", "-", "-"] ["0", "0", "0"]を用意する。

000 1 右にシフト　100
000 2 右にシフト　 10
000 3 右にシフト　  1
-------------------
001 1 右にシフト
000 2 右にシフト　010
000 3 右にシフト　001
-------------------

"""