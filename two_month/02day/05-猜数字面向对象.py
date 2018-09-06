class guessnum():
    def guessnumber(self):
        import random
        number = random.randint(1,101)
        for i in range(10):
            py = int(input('请输入一个数字：'))
            if number > py:
                print('猜小了')
            elif number < py:
                print('猜大了')
            else:
                print('猜对了')
                break
caishuzi = guessnum()
caishuzi.guessnumber()
