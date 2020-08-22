#bit全探索?
#あーこれ普通にとけるやつやーーーん、惜しいけど惜しくない罪、
#脳筋、プログラムやん
#配列つかって、各nにたいする組み合わせ個数を追加していく。
#そして最後にfor文で回して表示させる！
"""
N = int(input())
ans = []
for n in range(1, N+1):
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1,101):
                if x**2 + y**2 + z**2 + x*y + y*z + z*x == n:
                    ans+=1
    print(ans)
    ans=0
"""
    
"""
とりあえず書き出して行こうやん
"""

n = int(input())
#最初にリストの数を決めておく！
ans = [0 for _ in range(10050)]
for i in range(1,105):
	for j in range(1,105):
		for k in range(1,105):
			v = i*i+j*j+k*k+i*j+j*k+k*i;
			if v<10050:
				ans[v]+=1
for i in range(n):
	print(ans[i+1])