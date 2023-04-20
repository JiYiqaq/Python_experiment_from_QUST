def day_between(date1,date2):
    """计算两个日期之间的间隔"""
    minus = date2 - date1
    if minus.days > 0:
        return f"还有{minus.days}天"
    else:
        return f"已经过了{-minus.days}天"
from datetime import datetime
def day_input():
    """用于输入纪念日名称和日期，保存在字典中"""
    day_dict = {}
    while True:
        holiday = input("请输入节日名称：")
        if holiday == "":
            break
        day = input("请输入日期，格式写成‘年-月-日’的形式：")
        day_dict[holiday] = day
        break
    return day_dict
def day_between(date1,date2):
    """计算两个日期之间的间隔"""
    minus = date2 - date1
    if minus.days > 0:
        return f"还有{minus.days}天"
    else:
        return f"已经过了{-minus.days}天"
def display(result_dict):
    """用于展示最终结果"""
    print("*"*40)
    for holiday,count in result_dict.items():
        print(f"距离{holiday}{count}")
    print("*"*40)
if __name__ == "__main__":
    input_dict = day_input()
    today = datetime.now()
    today = today.strftime("%Y-%m-%d")
    today = datetime.strptime(today,"%Y-%m-%d")
    count_dict = {}
    for key,value in input_dict.items():
        value = datetime.strptime(value,"%Y-%m-%d")
        result = day_between(today,value)
        count_dict[key] =result
    display(count_dict)
