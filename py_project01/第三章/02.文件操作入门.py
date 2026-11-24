# #读文件
# # 1.打开文件
# f = open("./resources/静夜思.txt", "r", encoding="utf-8")
# # 2.读取文件内容
# # content = f.read() #读取所有内容
# # print(content)
#
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip())
#
# # 3.关闭文件
# f.close()

# # 写文件
# # 1.打开文件
# f = open("./resources/悯农.txt", "w", encoding="utf-8")
#
# # 2.写入文件内容
# f.write("悯农(李绅)\n\n")
# f.write("锄禾日当午，\n")
# f.write("汗滴禾下土。\n")
# f.write("谁知盘中餐，\n")
# f.write("粒粒皆辛苦。\n")
#
# # 3.关闭文件
# f.close()

# #############################释放资源 方式一######################################
# # 写文件
# # 1.打开文件
# f = open("./resources/悯农.txt", "w", encoding="utf-8")
#
# try:
# # 2.写入文件内容
#     f.write("悯农(李绅)\n\n")
#     f.write("锄禾日当午，\n")
#     i = 1/0
#     f.write("汗滴禾下土。\n")
#     f.write("谁知盘中餐，\n")
#     f.write("粒粒皆辛苦。\n")
#
# finally:
#     print("关闭文件")
# # 3.关闭文件
#     f.close()

#############################释放资源 方式二(最佳实践)######################################
# 写文件
# 1.打开文件
with open("./resources/悯农.txt", "w", encoding="utf-8") as f:

# 2.写入文件内容
    f.write("悯农(李绅)\n\n")
    f.write("锄禾日当午，\n")
    f.write("汗滴禾下土。\n")
    f.write("谁知盘中餐，\n")
    f.write("粒粒皆辛苦。\n")

