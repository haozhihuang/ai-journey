# #字面量的写法
# print(100)
# print(3.14)
# print(True) #布尔（bool）--首字母大写
# print(False)
# print("Hello Python")
# print("------------")
# print("None")
#
#
# #布尔类型本质也是整数类型
# print(True+1) # 2
# print(False-1) # -1
#
# #变量
# num = 1116.1
# print(num)
#
# num2 = num + 1
# print(num2)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)
#
# a = True
# print(a)

# #案例
# base = 231
# incr = 888
# print("未来第一个月的播放总量：",base + incr)   #复制上一行ctrl+d
# print("未来第二个月的播放总量：",base + incr + incr)
#
# #案例升级
# base,incr = 231,888
# print("未来第一个月的播放总量：",base + incr)   #复制上一行ctrl+d
# print("未来第二个月的播放总量：",base + incr + incr)
#
# #案例2：现有两个变量，分别为：a=10, b=20,现需要将这两个变量值交换，然后输出到控制台
# a = 10
# b = 20
#
# c = a
# a = b
# b = c
# print(a,b)

#练习：现有三个变量，分别为：a = 100,b = 200,c = 300,现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b,并将其输出到控制台。
# a = 100
# b = 200
# c = 300
# d = a
# e = b
# f = c
# c=d
# a=e
# b=f
# print(c,a,b)

#法二：现有三个变量，分别为：a = 100,b = 200,c = 300,现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b,并将其输出到控制台。
a = 100
b = 200
c = 300
temp = c
c =  a
a = b
b = temp
print(c,a,b) 





