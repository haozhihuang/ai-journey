# #集合 set--> 无序，不可重复，可修改
# # 定义
# s1 = {1,2,3,4,5,6,7,8,9,1,3,5,7}
#
# print(s1)
# print(type(s1))
#
# # 定义空集合
# s2 = set()
# print(s2)
# print(type(s2))

# 常见方法：
# add(): 添加元素到集合
# s1={100,200,300,400,500,600,700,800}
# print(s1)
#
# s1.add(1200)
# print(s1)
#
# s1.remove(1200)
# print(s1)
#
# # pop():随机删除集合中和元素并返回
# e = s1.pop()
# print(e)
# print(s1)
#
# # clear():清空集合
# s1.clear()
# print(s1)
#
# s2 = {"A","B","C","D","E","X","Y"}
# s3 = {"C","E","Y","Z"}

football_set = {"哈哈","多多","徐睿","嘎子","李四","拉拉","刘谦","咕咕","嘎嘎"}
# 选择篮球的学生名单
basketball_set = {"李四","多多","吴用","露露","刘谦","哈哈","悠悠","图图","牛牛","五五","七七"}
# 选择法语的学生名单
french_set={"张三","李四","王五","赵丽","露露","多多","吴用","刘谦","璐璐","浮浮"}
# 选择艺术学生名单
art_set={"露露","李四","吴用","浮浮","嘎嘎","嘎子"}
# 1.找出同时选择了法语和艺术的学生
# 方式一:
fa_set = french_set.intersection(art_set)
print(f"同时选修了 法语 和 艺术 的学生:{fa_set}")

# 方式二: & -->交集
fa_set2 = french_set & art_set
print(f"同时选修了 法语 和 艺术 的学生:{fa_set2}")

# 2.找出同时选修了所有四门课程的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了所有四门课程的学生:{all_set}")

# 3.找出选择了足球,但是没有选修篮球的学生  -差集
# 方式一:
fb_set=football_set.difference(basketball_set)
print(f"选择了足球,但是没有选修篮球的学生: {fb_set}")

# 方式二: --->差集
fb_set2=football_set - basketball_set
print(f"选择了足球,但是没有选修篮球的学生: {fb_set2}")

# 方式三: 集合推导式 -->快速构建集合,语法 {要往集合中添加的数据 for s in set1 if 条件}
fb_set3={s for s in football_set if s not in basketball_set}
print(f"选择了足球,但是没有选修篮球的学生:{fb_set3}")

# 4.统计每一个学生选择的课程数量
# 4.1 获取到学生名单 -- 并集(|)
#  all_set = football_set.union(basketball_set).union(french_set).union(art_set)
all_set=football_set | basketball_set | french_set | art_set

# 4.2 获取每一个学生选择的课程数量
all_list = [*football_set, *basketball_set, *french_set, *art_set]

for s in all_list:
    print(f"{s}选择了{all_list.count(s)}课程")

