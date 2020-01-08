K, X = map(int, input().split())
l=list(range(X-K+1,X+K,1))
l=[str(a) for a in l]
l=" ".join(l)
print(l)

#これはいろいろ学びが深い
#参考
#https://note.com/azura35/n/ndf3194de0a74　リストをprintする方法
#https://techacademy.jp/magazine/19093 数列の生成