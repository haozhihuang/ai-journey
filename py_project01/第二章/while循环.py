# # 计算1-100之间所有偶数的累加之和
# tocal = 0
# i=1
# while i<100 :
#     if i%2==0:
#       tocal+=i
#     i = i+1
#     print(f"1-100之间的偶数之和：{tocal}")

#计算1-200之间所有奇数累加之和
tocal = 0
i=1
while i<200:
    if i%2 != 0:
        tocal+=i
    i+=1
    print(f"1-200之间所有奇数累加之和:{tocal}")


