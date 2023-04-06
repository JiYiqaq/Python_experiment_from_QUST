waste_dict = {
    "可回收垃圾":["玻璃","金属","塑料瓶","纸张","衣服"],
    "干垃圾":["餐巾纸","塑料袋","纸巾","纸尿裤","花盆","陶瓷"],
    "湿垃圾":["剩饭剩菜","瓜皮果核","花卉绿植","过期食品"],
    "有害垃圾":["电池","油漆桶","荧光灯管","废药品"],
    }
while True:
    search_waste = input("请输入您要查询的垃圾：")
    find = False
    if search_waste == "q":
        break
    for classify,waste in waste_dict.items():
        if search_waste in waste:
           find = True
           print(f"{search_waste}的类别是{classify}")
           print("-"*30)
    if find == False:
        print("没有找到该垃圾的分类，请自行判断")
        print("-"*30)
        for classify,waste in waste_dict.items():
            print(f"{classify}包括：",end="")
            for item in waste:
                if waste.index(item) == len(waste) - 1:
                    print(item)
                else:
                    print(item,end="，")
        print("-" * 30)
        while True:
            option = input("您是否希望将此垃圾加入到现有分类中呢(yes/no)？")
            if option == "yes":
                classify = input("您希望将垃圾加入到哪个类别？")
                try:
                    waste_dict[classify].append(search_waste)
                except KeyError:
                    print("您的输入有误，没有此类别")
                break
            elif option == "no":
                print("可以继续查询垃圾分类")
                break
            else:
                print("您的输入有误，请重新输入")

