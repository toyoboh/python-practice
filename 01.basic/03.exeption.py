def divide(a, b):
    try:
        print(f'計算結果： {a / b}')
    except ZeroDivisionError as e:
        print(e)
    # except TypeError as e:
    #     print(e)
    except TypeError as e:
        # 処理のスルー
        pass
    except:
        print("なにかしらのエラー")
    else:
        print('正常に計算できました。')
    finally:
        print("処理が終わりました。")

divide(10, 2)
