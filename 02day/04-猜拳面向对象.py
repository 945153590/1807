class guess():
    def guesshand(self):
        import random
        for i in range(10):
            pc = random.randint(1,3)
            player = int(input('请选择1、石头 2、剪刀 3、布：'))
            if player == 1 and pc == 2 or player == 2 and pc == 3 or player == 3 and pc == 1:
                print('player win')
                break
            elif player == pc:
                print('ping')
            else:
                print('pc win')
caiquan = guess()
caiquan.guesshand()
