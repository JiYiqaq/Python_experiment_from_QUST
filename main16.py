username = "小千"
password = "xiaoqian123"
user_status = False
type = input("请输入登入方式（社交账号或博客账号）：")
def login(login_type):
    def check(func):
        def wrapper(*args,**kwargs):
            global user_status
            if not user_status:
                if login_type == "社交账号" or login_type == "博客账号":
                    user = input("请输入用户名：")
                    pwd = input("请输入密码：")
                    if user == username and pwd == password:
                        user_status = True
                    else:
                        print("用户名或者密码错误！")
                else:
                    print("此登入方式无法使用！")
            if user_status:
                return func(*args,**kwargs)
        return wrapper
    return check
@login(type)
def chat():
    print("聊天")
@login(type)
def shop():
    print("购物")
if __name__ == "__main__":
    chat()
    shop()
