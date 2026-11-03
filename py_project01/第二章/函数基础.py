# # #函数定义
# #
# # def out_line():
# #     print("---------------------------------")
# #     print("---------------------------------")
# #
# # # 函数调用
# # out_line()
#
#
# # 函数的参数与返回值
# # 函数1：计算圆的面积 --半径
# # def circle_area(r):
# #     area = 3.14 * r**2
# #     return area
# #
# # area = circle_area(10)
# # print(area)
# #
# # 函数2：计算长方形的面积 --长，宽
# def rectangle_area(l,w):
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
# # help(rectangle_area)
# print(rectangle_area(10,20))
#
# # 函数3：计算圆的面积，周长-->如果返回值有多个，多个返回值之间用逗号分隔 ---》多个返回值会封装到元组之中  round-->保留几位小数
# def circle_area_len(r):
#     """
#     根据圆的半径计算圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积，圆的周长
#     """
#     return round(3.14*r*r,1),round(2*3.14*r,1)
#
# al = circle_area_len(10)
# print(al)
# print(type(al))
#
# area,len = circle_area_len(10)
# print(area)
# print(len)
#

# 函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()


