import math
def is_even(number):
    """判断一个数是否是偶数"""
    if number%2 == 0:
        return True
    else:
        return False
def is_prime(number):
    """判断一个数是否是素数"""
    if number < 2:
        return False
    sqrt_number = int(math.sqrt(number))
    for i in range(2,sqrt_number+1):
        if number % i == 0:
            return False
    return True
def can_split(number):
    """判断一个数能否分解成两个素数的和，返回一个列表"""
    equo_list = []
    for i in range(1,number//2+1):
        j = number - i
        if is_prime(i) and is_prime(j):
            equo_list.append(f"{number}={i}+{j}")
    if not equo_list:
        equo_list.append(f"{number}无法分解成两个素数")
    return equo_list
if __name__ == "__main__":
    random_num = input("请输入一个大于5的偶数")
    if random_num.isdigit():
        random_num = int(random_num)
        if random_num > 5 and is_even(random_num):
            result_list = can_split(random_num)
            for equo in result_list:
                print(equo)
        else:
            print("输入的数字不符合要求！")
    else:
        print("请输入整数！")
