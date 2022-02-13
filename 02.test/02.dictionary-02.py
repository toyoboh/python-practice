# キーのみの表示
# 値の中にtokyoという文字列が存在するか
# すべてのキーと値の表示

dictionary = {
    'A': 'tanaka',
    'B': 'tarou',
    'C': 'man',
    'D': 'tokyo',
    'E': 'listening to music'
}

keys = dictionary.keys()
print(keys)


if 'tokyo' in dictionary.values():
    print("is there!")


for key, value in dictionary.items():
    print(f'{key}: {value}')

