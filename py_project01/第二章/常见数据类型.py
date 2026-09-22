# #常见数据类型  --> type() 获取指定的字面量或变量的类型
# print("hello")
# print(type("hello"))
#
# print(type(10))
# print(type(1.22))
# print(type(True))
# print(type(False))
# print(type(None))
#
# num = -199
# print(type(num))
#
# ##常见数据类型  --> isinstance(数据,类型) --> bool值 -->判定数据是否是指定的类型，如果是：Ture，否则False
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))
#
# #字符串
# # 定义字符串的三种方式
# s1 = "Hello" # 双引号定义
# s2 = 'World' #单引号定义（单双不能换行）
# s3 = """
# Hello:
#       我是黄浩
#       看我看我
#
# """  #三引号定义（多行字符串）
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# #定义字符串 --> It's very good
# #转义字符 \' \" \n \t
# msg = 'It\'s very good'
# print(msg)
# msg2 = "It's very good"
# print(msg2)
# msg3 = "zoo的意思是\"动物园\""
# print(msg3)
# msg4 = 'zoo的意思是"动物园"'
# print(msg4)
#
# print("\t你好呀我是黄浩！\n\t你是谁呀?") #\n 换行      \t   按了Tab缩进
#
#
#
# #字符串拼接
# s1 = "人生苦短" "我用Python" ",ok"
# print(s1)
#
# m1 ="人生苦短"
# m2 ="我用Python"
# print("我说："+m1+","+m2)
#
# #案例：-->str(int数字)-->将int类型的数字转为字符串
# name = "涛哥"
# age = 18
# pro = "软件工程"
# hobby = "Python、Java"
# print("大家好,我是"+name+",今年"+str(age)+"岁,学习的专业是"+pro+",爱好"+hobby)


#字符串格式化-->%s 占位符
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s" %(name,age,pro,hobby))

#字符串格式化 --> 方法二： f"内容{变量名/表达式}内容"  ------->推荐方式
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")
