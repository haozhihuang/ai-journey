# #列表操作
# # 定义    可以存储不同类型的元素，可重复，有序，元素可修改
# s=[56,90,88,65,90,"A","hello",True]
# print(type(s))
#
# # 访问列表的元素
# # 获取
# print(s[0]) #正向索引，从0开始
# print(s[-8])#反向索引，从-1开始
#
# print(s[2])
# print(s[-6])
#
# # 修改
# s[5] ="ABC"
# print(s)
#
# #注意：如果指定的索引超出范围将会报错 list assignment index out of range
# # s[10]="def"
# # print(s)
#
# # 删除
# del s[5]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)




# # --------------------------列表list切片------------------------------
# # # 定义列表
# # s=["A","B","C","D","E","F","G" ,"H" ,"I","J","K","L"]
# #
# # # 切片操作 s[开始索引：技术索引：步长]
# # print(s[0:5:1])
# # print(type(s[0:5:1]))
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[:5:2])
# print(s[0:-2:1])

# -----------------------列表list常用方法---------------------
# 列表定义
# s=[56,32,34,45,89,98,8,989,8678,67,32]
# print(s)
#
# # append():在列表尾部追加元素
# s.append(188)
# print(s)
#
# # insert():在指定索引之前输入元素
# s.insert(2,99)
# print(s)
#
# # remove():移除列表中第一个匹配的元素
# s.remove(32)
# print(s)
#
# # pop():删除列表中指定索引位置的元素并返回（如果未指定，默认删除最后一个）
#
# e=s.pop(1)
# print(e)
#
# e=s.pop()
# print(e)
#
# print(s)
#
# # sort():排序
# s.sort()
# print(s)
#
# # reverse():反转列表元素
# s.reverse()
# print(s)

#------------------------------------列表 list 案例--------------------------------------
# 案例1：将用户输入的10个数字，存储到一个列表中，
# 并将列表中的数字进行排序，输出其中的最小值、最大值 和 平均值。
# 1.定义列表
num_list=[]
# 2.将用户输入的十个数字存入列表
for i in range(10):
    num=int(input("请输入一个有效的数字："))
    num_list.append(num)

print("数字列表",num_list)
# 3.排序
num_list.sort()
print("排序后的数字列表：",num_list)

# 4.输出其中的最小值，最大值和平均值   ----->sum() 求和；-------->len() 获取元素的个数(列表的长度)
print("最小值：", num_list[0])
print("最大值：", num_list[-1])
print("平均值：", sum(num_list)/len(num_list))
