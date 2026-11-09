# #定义类 ------> 不推荐 动态的为对象添加属性
# class Car:
#     pass
#
# # 创建对象
# c1 = Car()
# # 动态的为对象添加属性
# c1.color = "red"
# c1.brand = "XIAOMI"
# c1.name = "yu7GT"
# c1.price = 550000
#
# print(c1)
# print(c1.brand)
# print(c1.__dict__) #会将对象中的所有属性以字典的形式输出出来
from os import write

from 函数进阶2 import total


# 定义类
# class Car:
#     #__int__方法是初始化的方法,会在对象创建时自动化调用,可以在该方法中设置对应的属性;
#     # self:是第一个参数,表示当前所创建出来的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕.")
#
# # 创建对象
# c1 = Car("红色","XIAOMI","yu7GT",550000)
# print(c1.__dict__)
#
# c2 = Car("白色","BMW","X7",650000)
# print(c2.__dict__)




# ---------------------------------------------定义类 实例方法-------------------------------------------------------
class Car:
    def __init__(self,c_color,c_brand, c_name,c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")

    # 定义实例方法
    def running(self):
        print(f"{self.c_brand} {self.c_name} 正在高速行驶中……")

    def total_cost(self,discount,rate=0.1):
        """
        计算提车的总费用，包含两个部分：车的价格，税费
        :param discount: 折扣
        :param rate: 税费
        :return: 提车的总费用
        """
        total_cost = self.c_price * discount + rate * self.c_price
        return total_cost

#测试
c1 = Car("红色","XIAOMI","yu7GT",550000)

# 调用对象中的方法
c1.running()

total1 = c1.total_cost(0.9,0.1)
print("提车的总费用为：", total1)

total2 = c1.total_cost(0.9)
print("提车的总费用为：", total2)




















