#if条件判断：如果分数超过680，我就去清华读书
# score = 700
# if score >= 680:
#     print("欢迎你来到大连交通大学！")
#     print("也恭喜你进入精彩的大学生活！")
# print("------------")

#if案例完成b站登陆功能的实现
#1.接受用户输入的账号和密码
ok_account = "188888888"
ok_password = "666666"
#2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
account = input("请输入您的账号：")
password = input("请输入您的密码：")
if account == ok_account and password == ok_password:
    print("登陆成功！")
    print("进入b站")
#3.判断账号和密码是否有错误的，如果任何一个错误，则登陆失败，提示错误信息
if account != ok_account or password != ok_password:
    print("登陆失败")
    print("账号或密码错误！！")