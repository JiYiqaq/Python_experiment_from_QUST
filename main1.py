import math
import turtle

# 设置画布大小
turtle.setup(width=600, height=400)

# 创建画笔
pen = turtle.Turtle()

# 设置画笔属性
pen.pensize(3)
pen.pencolor('red')

# 绘制左侧心形
pen.penup()
pen.goto(-100, 0)
pen.pendown()


# 绘制右侧心形
pen.penup()
pen.goto(-0, 50)
pen.pendown()
for i in range(200):
    # 计算心形函数的值

    t = i / 100 * 3.14
    x = 16 * (math.sin(t)) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

    # 将坐标转换为画布坐标系
    pen.goto(-x * 10, y * 10)


# 隐藏画笔
pen.hideturtle()

# 点击关闭窗口
turtle.exitonclick()