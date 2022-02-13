# l = [1, 20, 4, 50, 2, 1, 2]
# print(l)       # >>> [1, 20, 4, 50, 2, 1, 2]
# print(l[0])    # >>> 1
# print(l[-1])   # >>> 2
# print(len(l))  # >>> 7

# # 文字からリストに（あまり使わない）
# s = "abcdefg"
# print(list(s)) # >>> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # ２つ飛ばし
# print(n[::2])  # >>> [1, 3, 5, 7, 9]
# # ぎゃくから
# print(n[::-1]) # >>> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# # ネストした配列
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)       # >>> [['a', 'b', 'c'], [1, 2, 3]]

# # リスト
# s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # はいれつは置き換え可能
# s[0] = 'x'
# print(s)       # >>> ['x', 'b', 'c', 'd', 'e', 'f', 'g']

# s[2:5] = ['C', 'D', 'E']
# print(s)       # >>> ['x', 'b', 'C', 'D', 'E', 'f', 'g']

# s[2:5] = []
# print(s)       # >>> ['x', 'b', 'f', 'g']

# n = [1, 2, 3]
# n.append(4)
# print(n)       # >>> [1, 2, 3, 4]

# # 先頭代入
# n.insert(0, 200)
# print(n)       # >>> [200, 1, 2, 3, 4]

# # 取り出し
# n.pop()        # >>> 4
# print(n)       # [200, 1, 2, 3]

# # 先頭取り出し
# n.pop(0)       # >>> 200
# print(n)       # >>> [1, 2, 3]

# # 削除方法
# n = [1, 2, 3, 4, 5, 6]
# del n[0]
# print(n)       # >>> [2, 3, 4, 5, 6]
# # 注意
# # delは強力なので、変数自体を指定してしまうと未定義（削除される）となる
# n = [1, 2, 3]
# del n
# # print(n)       # >>> NameError: name 'n' is not defined

# # 一致したものを削除
# n = [1, 2, 2, 2, 3]
# n.remove(2)
# print(n)       # >>> [1, 2, 2, 3]
# n.remove(2)
# print(n)       # >>> [1, 2, 3]

# # 配列の結合
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# print(a + b)   # >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 別な方法（拡張:extend）
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 10]
# x.extend(y)
# print(x)       # >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 配列内検索
# r = [1, 2, 3, 4, 5, 1, 2, 3]
# print(r.index(3, 4))   # >>> 7 また、存在しない値の場合 Value Error が発生するので注意
# print(r.count(3))      # >>> 2
# # 配列内に存在するか
# if 5 in r:
#     print('exist')

# # ソート
# r.sort()
# print(r) # >>> [1, 1, 2, 2, 3, 3, 4, 5]
# # 逆（パターン１）
# r.sort(reverse=True)
# print(r) # >>> [5, 4, 3, 3, 2, 2, 1, 1]
# # 逆（パターン２）
# r.reverse()
# print(r) # >>> [1, 1, 2, 2, 3, 3, 4, 5]

# # 区切り文字指定で配列に格納
# s = 'My name is Mike.'
# to_split = s.split(' ')
# print(to_split)     # >>> ['My', 'name', 'is', 'Mike.']
# # 配列を指定した区切り文字で文字列に変換
# x = ' '.join(to_split)
# print(x)            # >>> My name is Mike.
# print(to_split)     # >>> ['My', 'name', 'is', 'Mike.'] なお、strメソッドのjoinは参照渡しではないので被破壊的メソッドである

# # list型のヘルプ表示
# # print(help(list))

# # 参照渡しについて
# i = [1, 2, 3, 4, 5]
# j = i
# print('i = ', i)   # >>> i =  [1, 2, 3, 4, 5]
# print('j = ', j)   # >>> j =  [1, 2, 3, 4, 5]

# j[0] = 100         # iまで変更されてしまう
# print('i = ', i)   # >>> i =  [100, 2, 3, 4, 5]
# print('j = ', j)   # >>> j =  [100, 2, 3, 4, 5]

# # そもそも代入とは変数にidentityを入れること
# # identityとは書くオブジェクトが持っている番号で
# # Pythonは内部で処理を実行する時にidentityを使ってオブジェクトを識別している


# seat = []
# min = 0
# max = 5
# print(min <= len(seat) < max)
# seat.append('p')
# seat.append('p')
# seat.append('p')
# seat.append('p')
# print(min <= len(seat) < max)
# seat.append('p')
# print(min <= len(seat) < max)


# # タプル(tuple)
# # 値の代入などできない（読み込み専用のイメージ）
# # countとindexとかしかない（helpで参照できる）
# # だけど、
# t = (1, 2, 3, 4, 1, 2)
# print(type(t))
# print(t)

# print(t.index(1))    # >>> 0
# print(t.count(1))    # >>> 2

# # 以下はエラーとなるが、タプルの中にリストを入れている場合は
# # リストを変更することはできる
# # t[0] = 2
# # print(t)             # >>> error

# x = ([1, 2, 3], [4, 5, 6])
# print(x)               # >>> ([1, 2, 3], [4, 5, 6])

# x[0][0] = 100
# print(x)               # >>> ([100, 2, 3], [4, 5, 6]) タプル自体の更新はできないことを覚えておく

# # タプルのアンパッキング（変数定義）
# num_tuple = (10, 20)
# print(num_tuple)  # (10, 20)

# x, y = num_tuple
# print(x, y)       # 10 20

# x, y = (10, 20)
# print(x, y)       # 10 20

# x, y = 10, 20
# print(x, y)       # 10 20

# # なお、上記は「()」をなくしても定義できる
# # Pythonの中身としては、タプルを展開しているイメージ

# # タプルを使えば入れ替えも簡単にできる
# # 普通なら
# i = 10
# j = 20
# tmp = i
# i = j
# j = tmp
# print(i, j)      # >>> 20 10
# # タプルを使うと
# a = 100
# b = 200
# print(a, b)      # >>> 100 200
# a, b = b, a
# print(a, b)      # >>> 200 100

# chose_from_two = ('A', 'B', 'C')

# answer = []
# answer.append('A')
# answer.append('C')

# print(chose)
