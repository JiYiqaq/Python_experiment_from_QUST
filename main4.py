a=int(input("请输入一个数:"))
num1=a
num=0
while num1>0:
    num=num*10+num1%10
    num1//=10
if a==num:
    print("{}是回文数".format(a))
else:
    print("{}不是回文数".format(a))
