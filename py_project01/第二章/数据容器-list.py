#列表操作
# 定义    可以存储不同类型的元素，可重复，有序，元素可修改
s=[56,90,88,65,90,"A","hello",True]
print(type(s))

# 访问列表的元素
# 获取
print(s[0]) #正向索引，从0开始
print(s[-8])#反向索引，从-1开始

print(s[2])
print(s[-6])

# 修改
s[5] ="ABC"
print(s)

#注意：如果指定的索引超出范围将会报错 list assignment index out of range
# s[10]="def"
# print(s)

# 删除
del s[5]
print(s)

# 遍历
for item in s:
    print(item)