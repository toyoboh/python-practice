# 辞書データからpopメソッドを使って、要素Aと要素Bを削除
# また、要素の全削除(clear)

dictionary = {
    'A': 'tanaka',
    'B': 'tarou',
    'C': 'man',
    'D': 'tokyo',
    'E': 'listening to music'
}

print(dictionary)

# 削除
dictionary.pop('A')
dictionary.pop('B')
print(dictionary)


# 全削除
dictionary.clear()
print(dictionary)
