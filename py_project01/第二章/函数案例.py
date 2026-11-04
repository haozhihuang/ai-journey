# # 案例1:定义一个函数：根据传入的低和高计算三角形面积的函数
# def triangle_area(b,h):
#     """
#     根据传入的低和高计算三角形面积
#     :param b: 底长
#     :param h: 高
#     :return: 三角形面积
#     """
#     return b * h / 2
# print("底长为30，高为20的三角形面积：",triangle_area(30,20))
#
# # 案例2：定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
# def count_aeiou(s):
#     num = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#             num += 1
#     return num
# print(count_aeiou("Hello Python Hello World OK"))
#
#
#
#
# #案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留一位小数），并返回
# def calc_score(score_list):
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list)/len(score_list),1)
#     return max_s, min_s, avg_s
#
# s_list = [589,609,605,643,677,455,477,489,503]
# max_score,min_score,avg_score=calc_score(s_list)
# print("最高分：",max_score)
# print("最低分：",min_score)
# print("平均分：",avg_score)











#
#
# # 1. 定义函数，根据传入的分数计算对应的等级：分数 ≥ 90 为 A，≥ 75 为 B，≥ 60 为 C，< 60 为 D。
# def level(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# print(level(100))   # A
# print(level(85))    # B
# print(level(60))    # C
# print(level(59))    # D
#
#
# # 2. 定义函数，判断一个字符串是否为回文串（通过反转字符串后与原字符串比较来实现），例如 "level"、"radar"，以及中文回文 "黄山落叶松叶落山黄"。
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("level"))
# print(is_palindrome("radar"))
# print(is_palindrome("黄山落叶松叶落山黄"))
# print(is_palindrome("abcd"))
#
#
# # 3. 定义函数，把传入的秒数换算成小时、分钟和秒。
# def convert(seconds):
#     hour = seconds // 3600
#     minute = seconds % 3600 // 60
#     second = seconds % 60
#     return hour, minute, second
#
# print(convert(3661))
# print(convert(59))
#
#
# # 4. 定义函数，根据三角形三条边的长度判断它的类型：等边三角形、等腰三角形、普通三角形，或者无法构成三角形。
# def type(a, b, c):
#     if a + b <= c or a + c <= b or b + c <= a:
#         return "无法构成三角形"
#     if a == b == c:
#         return "等边三角形"
#     if a == b or a == c or b == c:
#         return "等腰三角形"
#     return "普通三角形"
#
# print(type(3, 3, 3))
# print(type(3, 3, 5))
# print(type(3, 4, 5))
# print(type(1, 1, 5))



# --------------------------- 函数 - 变量的作用域 ---------------------------
# 全局变量 ：在函数外部 或 函数的内部都是可以访问的
num = 100

# 定义函数
def circle_area(r):
    # 局部变量：只能在函数内部使用
    pi = 3.14
    area = pi * r * r


    global num
    num = 10000
    print("num = ", num) # 10000


    return area


# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ", num) # 10000









