"""
https://note.com/tanon_cp/n/neda8607cfa7b
https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2020-05-31abc-169
"""

"""
A, B = input().split()
A = int(A)
#さきに小数点以下を切り捨てる、掛け算してからでは遅い
B = float(B) * 100
print(A*B // 100)
"""


#うーん、なるほど
import decimal

a, b = input().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)
print(int(a*b))
