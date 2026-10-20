# # for循环：遍历输入的字符串
#
# msg = input("请输入需要遍历的字符串：")
#
# for s in msg:
#     print(f"元素：{s}")
# else:
#     print("遍历结束！")

# range(end) ->获取一个从0开始，不包含end
# range(start,end) ->获取一个从start开始不包含end
# range(start,end,step) ->获取从start开始不包含end，step为步调。range(0,10,2)获得的数据为0，2，4，6，8
# 案例1：计算1-100之间所有奇数之和
# total = 0
#
# for i in range(1,101):
#     if i % 2 == 1 :
#         total += i
# print("1-100之间所有奇数之和为：",total)

# # 简化
# total = 0
#
# for i in range(1,101,2):
#         total += i
# print("1-100之间所有奇数之和为：",total)

# 案例2：计算100-500之间所有3的倍数的数字之和
# total = 0
#
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print("100-500之间所有3的倍数的数字之和:", total)

"""如下：是一个长度为5宽度为3的长方形
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
"""

# print("*") :自带换行效果，每一次执行都会输出新的一行中
#  print("*", end="")：end表示的是每一次输出以什么结束：默认:\n,表示换行
#1.接受键盘输入 m，n
#长度
# m = int(input("请输入长方形的长度："))
# #宽度
# n = int(input("请输入长方形的宽度："))

# # 打印长方形
# for i in range(n):#控制行
#     for i in range(m):#控制列
#        print("*", end="")
#     print()

# # 嵌套循环案例：打印99乘法表
# for i in range(1,10): #外层循环 - 控制行
#     for j in range(1,i+1):
#         print(f"{j}×{i}={j*i}",end="\t ")
#     print()

# # 根据输入的直角边的变长，打印等腰直角三角形
# n=int(input("请输入直角边边长："))
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print()

# 根据输入的数字打印对应的数字金字塔
n=int(input("请输入数字："))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="\t ")
    print()