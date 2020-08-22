
K = int(input())
"""
count = 1
a = "7"
while int(a) % K != 0:
    a = a + "7"
    count += 1
print("-1")
"""
"""
ans = 1
i = 1

if K%2 == 0 and K%5 == 0:
    print("-1")
    
while 10**i % 9*K != 0:
    ans += 1
    i += 1
print(ans)
"""

f=0
n=K

for i in range(10**6 + 1):
    if n == 0:
        f=1
        print(i)
        break
    n = ((n*10) + 7 ) % K
    
if f==0:
   print(-1)