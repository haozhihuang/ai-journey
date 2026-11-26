# 读文件
"""
路径的写法：
1.相对路径：从当前文件所在目录开始查找（推荐）
          .; 表示当前目录 -----> ./resources/悯农.txt  ./可以省略
          ..; 表示上一级目录 -----> ../第二章/File/嘟嘟嘟.txt -->../../第二章/File/嘟嘟嘟.txt
2.绝对路径：从根目录开始查找,文件位置的完整路径（注意：绝对路径中，路径分隔符必须使用双反斜杠\\）
          D:\\ai-journey\\py_project01\\第三章\\resources\\静夜思.txt
          D:/ai-journey/py_project01/第三章/resources/静夜思.txt ----->也可以
"""
with open("D:\\ai-journey\\py_project01\\第三章\\resources\\静夜思.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
# with open("../第二章/File/嘟嘟嘟.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)
# with open("resources/悯农.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)


#写文件
# with open("resources/望庐山瀑布.txt", "w", encoding="utf-8") as f:
#     f.write("望庐山瀑布\n")
#     f.write("日照香炉生紫烟，")
#     f.write("遥看瀑布挂前川。")
#     f.write("飞流直下三千尺，")
#     f.write("疑是银河落九天。")

# a：append追加，追加到文件末尾
with open("resources/望庐山瀑布.txt", "a", encoding="utf-8") as f:
    f.write("望庐山瀑布\n")
    f.write("日照香炉生紫烟，")
    f.write("遥看瀑布挂前川。")
    f.write("飞流直下三千尺，")
    f.write("疑是银河落九天。")
