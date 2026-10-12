#if条件判断：如果分数超过680，我就去清华读书
# score = 700
# if score >= 680:
#     print("欢迎你来到大连交通大学！")
#     print("也恭喜你进入精彩的大学生活！")
# print("------------")

# #if案例完成b站登陆功能的实现
# #1.接受用户输入的账号和密码
# ok_account = "188888888"
# ok_password = "666666"
# #2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
# if account == ok_account and password == ok_password:
#     print("登陆成功！")
#     print("进入b站")
# #3.判断账号和密码是否有错误的，如果任何一个错误，则登陆失败，提示错误信息
# if account != ok_account or password != ok_password:
#     print("登陆失败")
#     print("账号或密码错误！！")


# #if...else...案例完成b站登陆功能的实现
# #1.接受用户输入的账号和密码
# ok_account = "188888888"
# ok_password = "666666"
# #2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
# if account == ok_account and password == ok_password:
#     print("登陆成功！")
#     print("进入b站")
# else:
#     print("登陆失败")
#     print("账号或密码错误！！")


# #  案例1 ：根据用户输入的年份，判断这一年是闰年还是平年
# year = int(input("请输入需要判定的年份："))
# # 如果是非整百年份，且能被4整除 就是闰年；整百年份，必须被400整除 也是闰年
# if (year %100 == 0 and year%4 == 0) or (year%400 == 0):
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 是平年")

# # 根据用户输入的数字，判断奇偶
# num = int(input("请输入数字："))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

# # 根据用户输入的年龄，判断用户是否已经成年
# age=int(input("请输入年龄："))
# if age >= 18:
#     print(f"{age}成年")
# else:
#     print(f"{age}未成年")

# # 根据用户输入的数字，判断该数字是正数还是负数(不考虑0)
# num=int(input("输入一个数字："))
# if num > 0:
#     print(f"{num}是正数")
# else:
#     print(f"{num}是负数")

# # 根据用户输入的考试分数，判断该分数是否及格了（>60及格）
# num=int(input("输入一个数字："))
# if num > 60:
#      print(f"{num}及格了")
# else:
#      print(f"{num}没及格")

# 根据用户输入的数字，判断该数字是正数还是负数(考虑0)
# num=int(input("输入一个数字："))
# if num > 0:
#      print(f"{num}是正数")
# elif num < 0:
#      print(f"{num}是负数")
# else:
#      print(f"{num}是0")

# 根据输入的用户名、密码进行登陆系统
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username == "admin" and password == "666888":
#     print("登陆成功")
# elif username == "root" and password == "555555":
#     print("登陆成功")
# elif username == "laozhang" and password == "555666":
#     print("登陆成功")
# else:
#     print("登录失败")

# 根据输入的购物车的商品价格总额，以及如下的折扣规则，计算实际支付的金额
# 金额 >=500:8折
# 300 <=金额<500:9折
# 100 <=金额<300:95折
# 金额<100:无折扣
a = float(input("请输入金额："))
if a >= 500:
    pay=a*0.80
elif 300<=a<500:
    pay=a*0.90
elif 100<=a<300:
    pay=a*0.95
else:
    pay=a
print(f"实际金额{pay}")