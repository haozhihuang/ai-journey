import json

# # 写入json数据文件
# user = {
#     "name": "张三",
#     "age": 18,
#     "gender": "男",
#     "hobbies":["reading", "traveling", "swimming"]
# }
# with open("resources/user.json", "w", encoding="utf-8") as f:
#     # ensure_ascii=False: 确保所有的数据输出的数据都是ascii编码（非ASCII码会进行转义）；False，# 非ASCII码保留原样输出
#     # indent=2: 美化json数据，设置缩进为2个空格（格式化）
#     json.dump(user, f, ensure_ascii=False, indent=2)


# 读取json数据文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
