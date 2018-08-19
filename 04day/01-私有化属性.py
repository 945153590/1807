class Dog():
    def __init__(self):
        self.name = ''
        self.__age = 0

    def sleep(self):
        print('睡觉')

    def setAge(self,age):
        if age > 15 or age < 1:
            print('年龄不符合')
        else:
            self.__age = age
    def getAge(self):
        return self.__age

erha = Dog()
erha.sleep()
erha.setAge(10)
print(erha.getAge())
