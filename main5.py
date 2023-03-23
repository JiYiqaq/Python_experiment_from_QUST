products=[("鸡蛋",1),("牛奶",2),("苹果",2),("香蕉",3)]
shopping_list=[]
money=float(input("请输入您的购物资金:"))
while True:
    print("*"*20)
    print("商品列表如下:")
    for index,item in enumerate(products):
        print("{}.商品:{},价格:{}".format(index+1,item[0],item[1]))
    print("*"*20)
    option=input("请输入您要购买的商品(退出请键入q):")
    if option.isdigit():
        option=int(option)
        if 0<=option-1<len(products):
            option_product=products[option-1]
            if option_product[1]<=money:
                shopping_list.append(option_product)
                money-=option_product[1]
                print("购买成功!")
            else:
                print("您的余额不足!")
        else:
                print("您购买的商品不存在!")
    elif option=="q":
            print("-"*10,"购物清单","-"*10)
            for i in shopping_list:
                print("已购商品:{},价格:{}".format(i[0],i[1]))
            print("您的余额为:",money)
            break
    else:
            print("你的输入不合法!")