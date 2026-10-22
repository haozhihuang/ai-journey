# # 案例1：根据输入的用户名密码执行登录操作，具体要求如下：
# #
# # 正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
# # 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
# # 输入的用户名和密码不能为空！
# # 登录成功：输出 "登录成功，进入B站首页~"
# # 登录失败：输出 "用户名或密码错误，请重新输入！"
#
# """关键字:
#         break:只能出现在循环中，表示结束，跳出循环的含义（break跳出循环时，while后面的else中的代码将不会执行）
#         continue:只能够出现循环中，表示中断本次循环，直接进入下一次循环
# """
#
# while True:
#     # 1.接收输入的用户名和密码
#     username = input("请输入正确的用户名：")
#     userpassword = input("请输入正确的密码：")
#
#     # 2.校验输入的用户名名和密码不能为空
#     if username=="" or userpassword=="":
#         print("输入的用户名和密码不能为空！！！请重新输入")
#         continue #结束当前循环直接进入下一轮循环
#     # 3.判断用户名和密码的正确性，执行登陆操作
#     if username=="admin" and userpassword=="666888":
#         print("登录成功，进入B站首页~")
#         break # 跳出循环
#     elif username=="dududu" and userpassword=="666999":
#         print("登录成功，进入B站首页~")
#         break # 跳出循环
#     elif username=="lalala" and userpassword=="666666":
#         print("登录成功，进入B站首页~")
#         break # 跳出循环
#     else:
#         print("用户名或密码错误，请重新输入")

# 需求:用户名密码登录，正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666，5次登录机会，输入错误五次，不允许再操作了。
i=0
while i<5:
  username = input("请输入正确的用户名：")
  userpassword = input("请输入正确的密码：")

  if username == "" or userpassword == "":
      print("用户名和密码不能为空请重新输入！")
      continue
  elif username == "admin" and userpassword == "666888":
      print("登录成功，进入B站首页~")
      break
  elif username == "zhangsan" and userpassword == "123456":
      print("登录成功，进入B站首页~")
      break
  elif username == "taoge" and userpassword == "888666":
      print("登录成功，进入B站首页~")
      break
  i += 1
  if i < 5:
      print(f"用户名或密码错误，请重新输入，您还有{5 - i}次机会")
  else:
      print("5次机会已用完，不允许再操作了！")