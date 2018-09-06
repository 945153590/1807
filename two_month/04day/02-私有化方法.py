class QQ():

    def __openvip(self):
        print('开会员成功')

    def vip(self,money):
        if money > 10:
            self.__openvip()
        else:
            print('失败')


qq = QQ()
qq.vip(5)
qq.vip(13)
