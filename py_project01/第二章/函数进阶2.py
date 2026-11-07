# #---------------------------------------案例-----------------------------------------
# # 案例1：计算n的阶乘
# # 递归调用(先层层递进，再逐层回归)：指的是在函数中自己调用自己的情况 -----> 一定得有终结点
# """
# jc(10) = 10 * jc(9)
# jc(9) = 9 * jc(8)
# jc(8) = 8 * jc(7)
# jc(7) = 7 * jc(6)
# jc(6) = 6 * jc(5)
# jc(5) = 5 * jc(4)
# jc(4) = 4 * jc(3) = 4*6=24
# jc(3) = 3 * jc(2) = 3*2=6
# jc(2) = 2* jc(1) = 2*1=2
# jc(1) = 1
# """
# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n * jc(n-1)
#
# result = jc(10)
# print(result)


"""
案例2：案例2：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
具体规则如下：
    1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
    2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def calc_order_cost(*args:tuple[str,float,int],coupon :int=0,score:int=0,express:float=0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
    :param args:商品信息（商品名，价格，数量） --->如：("鼠标",188,2)
    :param coupon:优惠券
    :param score:积分
    :param express:运费
    :return: 订单的总金额
    """
    #订单的总金额 = 商品总金额 = 优惠券-积分抵扣+运费
    # 1.计算商品总金额
    total_price = [goods[1] *goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    # 3. 扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    # 4. 添加运费
    total_cost += express

    return total_cost

# 测试
# total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 3999, 1), coupon=10, score=4000, express=9.9)
# print(total)

# total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), coupon=10, score=4000, express=9.9)
# print(total)

# total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), express=9.9)
# print(total)

# 测试
total = calc_order_cost(("鼠标", 188.5, 2), ("键盘", 388, 1), ("手机", 6999, 1))
print(total)






















