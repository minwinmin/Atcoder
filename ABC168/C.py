
def check(learn_total):
    for i in range(m):
        if learn_total[i] < x:
            return False
    return True
 
 
def calc_price(bit):
    price_total = 0  # 値段の合計
    learn_total = [0] * m  # 理解度
 
    for i in range(n):
        if (bit >> i) & 1:  # i桁目が0か1か見て、i番目を買うか買わないか判定します
            price_total += c[i]  # 買うので、i番目の値段を加算します
            print(price_total)
            learn = a[i]  # 「i番目の参考書を読んで増える、各アルゴリズムの理解度」のリストです
            print(learn)
            for j, le in enumerate(learn):  # 理解度を足します。 enumerateを使うと、range(n)よりスマートです
                learn_total[j] += le
                print(learn_total[j])
 
    # 条件を満たすか、check関数で確認します
    if check(learn_total):
        return price_total
    else:
        return INF
 
 
if __name__ == '__main__':
    INF = float("inf")
 
    n, m, x = list(map(int, input().split()))
 
    # 空のリストを作って、appendで追加していきます
    c = []  # 参考書の値段です
    a = []  # 各参考書に入る理解度です
 
    for i in range(n):
		# こうすると、2つ目以降をリストで受け取れます
		# *a_temp の意味
        c_temp, *a_temp = list(map(int, input().split())) 
        c.append(c_temp)
        a.append(a_temp)
 
    ans = INF
 
    for bit in range(1 << n):
        price = calc_price(bit)  # 条件を満たすなら価格、満たさないならINFが返ってきます
        ans = min(ans, price)  # 答えを更新します
 
    if ans == INF:
        print(-1)
    else:
        print(ans)