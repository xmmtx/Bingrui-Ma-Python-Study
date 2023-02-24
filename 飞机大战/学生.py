class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sleep(self):
        print(self.name,'在睡觉')
    def study(self):
        print(self.name,'在学习')
zhangSan=Student('张三',13)
zhangSan.sleep()
zhangSan.age=15
print(zhangSan.name,'的年龄是',zhangSan.age)
liSi=Student('李四',14)
liSi.study()