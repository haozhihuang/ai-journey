# #字典 --key：value--->key不能重复(如果重复，后面的值，会覆盖前面的值)、key必须得是不可变类型（str，int，float，tuple）
# # 定义字典
# dict1 = {'嘟嘟':888, '嘎嘎':666, '拉拉':688, '恰恰':999}
# print(dict1)
# print(type(dict1))
#
# #key必须得是不可变类型（str，int，float，tuple）,不能是 list、set、dict
# dict2 = {0:888, 1.5:666, (1,2):000, ('A','B'):999}
# print(dict2)
#
# # 访问
# print(dict1["嘟嘟"]) #获取
# dict1["嘟嘟"] = 555
# print(dict1)




# ------------------------------------------字典 常见操作--------------------------------------------------
# dict1 = {'嘟嘟':1, '拉拉':2, '丽丽':3, '强强':4}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["熊大"] = 5
# print(dict1)
#
# # key存在就是修改
# dict1["强强"]=6
# print(dict1)
#
# # 查询
# print(dict1["嘟嘟"])
# print(dict1.get("嘟嘟"))
#
# print(dict1.keys())#获取所有的key
# print(dict1.values())#获取所有的value
# print(dict1.items())#获取所有的键值对 key:value
#
# # 删除
# score=dict1.pop("丽丽")
# print(score)
# print(dict1)
#
# del dict1["拉拉"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
#
# for k,v in dict1.items():
#     print(f"{k}: {v}")


"""
案例：
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
具体功能如下：

1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5. 退出购物车

结构：shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""
# shopping_cart = {}
# menu = """
# ########## 购物车系统 ##########
# #       1. 添加购物车           #
# #       2. 修改购物车           #
# #       3. 删除购物车           #
# #       4. 查询购物车           #
# #       5. 退出购物车           #
# ###############################
# """
#
# print("欢迎使用购物车管理系统 ~")
#
# while True:
#     # 1. 制作菜单
#     print(menu)
#
#     # 2. 执行的具体操作
#     choice=input("请选择要执行的操作(1-5):")
#     match choice:
#         case "1":  # 添加购物车
#             goods_name = input("请输入商品名称：")
#             goods_price = float(input("请输入商品价格："))
#             goods_num = int(input("请输入商品数量："))
#
#             # 如果商品存在，则不执行添加，提示信息
#             if goods_name in shopping_cart:
#                 print("该商品已存在，请重新选择 ~")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("商品添加完毕 ~")
#         case "2":  # 修改购物车
#             goods_name = input("请输入要修改的商品名称：")
#             goods_price = float(input("请输入商品最新的价格："))
#             goods_num = int(input("请输入商品最新的数量："))
#             # 如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择 ~")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("商品修改完毕 ~")
#         case "3":  # 删除购物车
#             goods_name = input("请输入要删除的商品名称：")
#
#             # 如果商品不存在，则提示错误信息，重新选择
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择 ~")
#             else:
#                 del shopping_cart[goods_name]
#             print("商品删除完毕 ~")
#         case "4":  # 查询购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")
#         case "5": #退出购物车
#             pass
#         case _: #匹配其他所有情况
#             print("非法操作，不支持！！！")




"""
基于现有知识开发一个教务管理系统

开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：

1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5. 列出所有学生：遍历所有学生信息并输出。
6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7. 退出系统。
"""

students = {}

menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # #
#  1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""

while True:
    print(menu)
    choice = input("请选择要执行的操作(1~7): ")

    match choice:
        case "1":  # 添加学生信息
            name = input("请输入学生姓名：")
            if name in students:
                print(f"【{name}】已存在，请重新选择 ~")
                continue
            chinese = float(input("请输入语文成绩："))
            math = float(input("请输入数学成绩："))
            english = float(input("请输入英语成绩："))
            students[name] = {"chinese": chinese, "math": math, "english": english}
            print(f"添加【{name}】成功")

        case "2":  # 修改学生信息
            name = input("请输入要修改的学生姓名：")
            if name not in students:
                print(f"【{name}】不存在，请重新选择 ~")
                continue
            chinese = float(input("请输入语文成绩："))
            math = float(input("请输入数学成绩："))
            english = float(input("请输入英语成绩："))
            students[name] = {"chinese": chinese, "math": math, "english": english}
            print(f"修改【{name}】成功")

        case "3":  # 删除学生信息
            name = input("请输入要删除的学生姓名：")
            if name not in students:
                print(f"【{name}】不存在，请重新选择 ~")
                continue
            del students[name]
            print(f"删除【{name}】成功")

        case "4":  # 查询学生信息
            name = input("请输入要查询的学生姓名：")
            if name not in students:
                print(f"【{name}】不存在，请重新选择 ~")
                continue
            info = students[name]
            total = info["chinese"] + info["math"] + info["english"]
            print(f"姓名：{name}  语文：{info['chinese']}  数学：{info['math']}  "
                  f"英语：{info['english']}  总分：{total}  平均分：{total / 3:.1f}")

        case "5":  # 列出所有学生
            if not students:
                print("系统中暂无学生信息 ~")
                continue
            for name, info in students.items():
                total = info["chinese"] + info["math"] + info["english"]
                print(f"姓名：{name}  语文：{info['chinese']}  数学：{info['math']}  "
                      f"英语：{info['english']}  总分：{total}")
            print(f"共 {len(students)} 名学生")

        case "6":  # 统计班级成绩
            if not students:
                print("系统中暂无学生信息 ~")
                continue
            subjects = {"chinese": "语文", "math": "数学", "english": "英语"}
            for key, label in subjects.items():
                pairs = [(info[key], name) for name, info in students.items()]
                top_score = max(p[0] for p in pairs)
                low_score = min(p[0] for p in pairs)
                top_names = [p[1] for p in pairs if p[0] == top_score]
                low_names = [p[1] for p in pairs if p[0] == low_score]
                avg = sum(p[0] for p in pairs) / len(pairs)
                print(f"{label}  最高分：{top_score}（{'、'.join(top_names)}）  "
                      f"最低分：{low_score}（{'、'.join(low_names)}）  平均分：{avg:.1f}")

        case "7":  # 退出系统
            print("已退出教务管理系统 ~")
            break

        case _:
            print("非法操作，不支持！！！")


















