# # 2進数
# print(0b101) # >>> 5
# print(0B101) # >>> 5

# # 8進数
# print(0o7)   # >>> 7
# print(0O12)  # >>> 10

# # 16進数
# print(0xf)   # >>> 15
# print(0X13)  # >>> 19

# # 文字列
# print('I\'m Mike')

# # 文字列として\を表示する時には頭にrをつける
# print(r'test\nice\good')
# # か、\をもう一つつけたり
# print('test\\nice\good')

# # トリプルクォート
# print('''
# これだと
# 空白行が入る
# ''')

# print('''\
# これなら
# 空白行が入らない\
# ''')

# print('py''thon')     # >>> python
# prefix = 'py'
# print(prefix'thon') # >>> error 変数とはくっつけられない
# print('Hi,' * 3)      # >>> Hi, Hi, Hi
# s = ('aaaaaaaaaaaaaaaaaa'
#      'bbbbbbbbbbbbbbbbbb')
# print(s) # >>> aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbb

# s = 'aaaaaaaaaaaaaaaa' \
#     'bbbbbbbbbbbbbbbb'
# print(s)

# word = 'python'
# print(word[0])   # 先頭
# print(word[-1])  # 末尾

# # スライス(slice)
# print(word[0:2]) # >>> py
# print(word[3:])  # >>> hon

# # 先頭文字を書き換えた場合
# word = 'python'
# word[0] = "j"      # これはエラー
# new = 'j' + word[1:] # >>> jython
# print(new[:])        # >>> jython
# print(len(new))      # >>> 6 （文字数）

# # 配列について
# # 以下は参照渡しの例
# a = ["a"]
# b = a
# b.append("b")
# print(a)
# print(b)

# # 参照渡しを防ぐ方法は2つある
# # .copy　と　[:]　があるが、.copyの方がより直感的で読みやすい
# a = ["a"]
# b = a.copy()
# b.append("b")
# print(a)
# print(b)
# # または
# a = ["a"]
# b = a[:]
# b.append("b")
# print(a)
# print(b)

# # またテキストや数値などは参照渡しではなく値渡しとなる
# a = "a"
# b = a
# b = "b"
# print(a + ":" + b)

# # printについて
# print('Hi', 'Mike', sep=',') # カンマ区切りになる
# print('Hi', 'Mike', sep=':')
# print('Hi', end=".\n")       # 末尾もしていできる

# # 文字列メソッド
# # 先頭文字確認
# s = 'My name is Mike. Hi Mike.'
# is_start = s.startswith('My')
# print(is_start)                 # >>> True
# is_start = s.startswith('X')
# print(is_start)                 # >>> False
# # どこにあるか
# print(s.find('Mike'))

# # formatについて
# # ちなみにformatで数字を代入する場合、数値から文字へ変換される
# f = 'a is {}'.format('a')
# print(f)                          # >>> a is a

# f = 'My name is {1} {0}'.format('tanaka', 'tarou')
# print(f)

# name = 'tarou'
# family = 'tanaka'
# f = 'My name is {name} {family}'.format(name=name, family=family)
# f = 'My name is {family} {name}'.format(name=name, family=family)
# print(f)
# また、他にも以下のやりかたがある
name = 'tarou'
age  = 100
print('私は{name}。{age}歳です。'.format(name=name, age=age))
# 上記の簡潔版
print(f'私は{name}。{age}歳です。') # エフストリングス

# # 平方根もつかえたりする
# import math
# result = math.sqrt(25)
# print(result)
# print(type(result))

# # python ドキュメントも見れる
# print(help(math))
