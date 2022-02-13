# ##########################################################
# 1
# ##########################################################
# class Person:
#     def __init__(self, nationality):
#         self.nationality = nationality
    
#     def say_hello(self):
#         print(f'こんにちは、私の国籍は{self.nationality}です。')

# person = Person('日本')
# person.say_hello()


# ##########################################################
# 2 インスタンス生成
# ##########################################################
# class Person:
#     nationality = '日本'

#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print(f'こんにちは、私の国籍は{ self.nationality }です。')

#     def say_my_name(self):
#         print(f'私の名前は{ self.name }です。')

# tanaka = Person('田中')
# tanaka.say_hello()
# tanaka.say_my_name()


# ##########################################################
# 3 継承
# ##########################################################
# class Person:
#     nationality = '日本'

#     def __init__(self, name):
#         self.name = name
    
#     def say_hello(self):
#         print(f'こんにちは、私の国籍は{ self.nationality }です。')
    
#     def say_my_name(self):
#         print(f'私の名前は{ self.name }です。')

# class Kid(Person):
#     def say_hello(self, age):
#         print(f'私の名前は{ self.name }です。年齢は{ str(age) }歳です。')

# tanaka = Kid("たなか")
# tanaka.say_hello(9)

# ##########################################################
# 4 カプセル化
#   プライベートなものにするときは、先頭に「__」をつければ良い（アンダーバを２つ）
# ##########################################################
# class Person:
#     __nationality = '日本'

#     def __init__(self, name):
#         self.__name = name

#     def say_hello(self):
#         print(f'こんにちは、私の国籍は{ self.__nationality }です。')

#     def say_my_name(self):
#         print(f'私の名前は{ self.__name }です。')

# tanaka = Person("田中")
# tanaka.say_hello()
# tanaka.say_my_name()
