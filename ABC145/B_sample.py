N, S = int(input()), input()
print("NYoe s"[S[N//2:]==S[:N//2]::2])

#下記のコードはわかりやすい、コード長を短くする工夫の参考になる
n=int(input())//2
s=input()
print('Yes' if s[:n] == s[n:] else 'No')