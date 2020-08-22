"""
#なんか違う
import collections
import itertools

N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

counter = collections.Counter(S)
mode_v = counter.most_common()[0][-1]
it = itertools.takewhile(
    lambda kv : kv[-1] == mode_v, counter.most_common()        
)

print(*(k for k, v in it))
"""

"""
リスト(list)　[]
タプル(tuple)　()
辞書(dict)   {}
セット・集合(set)
http://www.tohoho-web.com/python/list.html
の違い
"""

"""
参考
https://note.com/tanon_cp/n/ne423915acdaa
"""

n=int(input())
arr=[input() for _ in range(n)]
dic={}
for i in range(n): #各単語の出現回数を数える
 if arr[i] not in dic:
   dic[arr[i]]=1
 else:
   dic[arr[i]]+=1
largest=max(dic.values()) #最大の出現回数を求める
ans=[]
for keys in dic.keys():
 if dic[keys]==largest: #出現回数が最も多い単語を集計する
   ans.append(keys)
ans=sorted(ans) #単語を辞書順に並べ替えて出力する
for words in ans:
 print(words)