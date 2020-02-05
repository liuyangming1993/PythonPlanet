#!/usr/bin/python
# coding:utf-8

"""计算每日摄入热量的工具"""
__author__ = 'Liu Yangming'

formatter_kcal = "{}kcal"
formatter_g = "{}g"


def bmr_male(weight, height, age):
    return (float(weight) * 13.7) + (5.0 * float(height)) - (6.8 * float(age)) + 66


def bmr_female(weight, height, age):
    return (weight * 9.6) + (1.8 * height) - (4.7 * age) + 655


def bmr(gender, weight, height, age):
    if gender == '男':
        return bmr_male(weight, height, age)
    elif gender == '女':
        return bmr_female(weight, height, age)


def daily_eat(aim, daily_use):
    if aim == 1:
        return daily_use + 500
    elif aim == 2:
        return daily_use


def daily_use(exercise_intensity, bmr):
    if exercise_intensity == 1:
        return bmr * 1.2
    elif exercise_intensity == 2:
        return bmr * 1.375
    elif exercise_intensity == 3:
        return bmr * 1.55
    elif exercise_intensity == 4:
        return bmr * 1.725
    elif exercise_intensity == 5:
        return bmr * 1.9
    else:
        return "输入错误，请填写序号1-5"


def get_aim_str(aim):
    if aim == 1:
        return "增肌"
    elif aim == 2:
        return "减脂"
    else:
        return "error"


def format_kcal(num):
    return formatter_kcal.format(num)


def format_g(num):
    return formatter_g.format(num)


def get_limit(aim):
    if aim == 1:
        return ""
    elif aim == 2:
        return "不多于"
    else:
        return "error"


def print_tips():
    print(f"""-----------------------------------------------------------------------------
附录：
营养成分摄入比例为碳水：蛋白质：脂肪=5：2：3
1g碳水=4kcal
1g蛋白质=4kcal
1g脂肪=9kcal
处于减脂状态时，每日摄入需要低于日常消耗，但不能低于基础代谢。
打开热量缺口要循序渐进，拿出1-3个星期的时间作为减脂过渡期，好让身体去适应，从而避免热量缺口过大影响基础代谢。
在减脂过渡期，第一周热量缺口100-200大卡，第二周热量缺口200-400大卡，留意体重的变化，每周瘦1-1.5斤是最合理的。
过了过渡期，如果感觉效果不是很好，可以再减100-200大卡的摄入，不断的自我调整，直到体重开始平稳下降。
热量换算公式：1Kcal约为4.2KJ
*****************************************************************************""")


print("为了给您定制饮食方案，请您先填写调查问卷……")
name = input("姓名：")
gender = input("性别：")
age = int(input("年龄："))
height = float(input("身高（cm）："))
weight = float(input("体重（kg）："))
print(f"""请选择您每日的运动情况：
1、几乎不运动：久坐少动，如办公室职员、司机。
2、活动量较小：一天中长时间站着，如护士、教师或者每周进行1-3天中强度训练。
3、活动量一般：一天中很多时间进行体力活动，如厨师、中餐厅服务员或者每周进行3-5天中强度训练。
4、活动量很大：一天中大部分时间在进行体力活动，如伐木工人或者每周6-7天强度训练。
5、活动量极大：专业运动员才会达到的水准。""")
exercise_intensity = int(input("您的选择："))
print(f"""您健身的目的是？
1、增肌
2、减脂""")
aim = int(input("您的选择："))
# 计算相应的值
bmr = bmr(gender, weight, height, age)
daily_use = daily_use(exercise_intensity, bmr)
daily_eat = daily_eat(aim, daily_use)
# 打印结果
print("*****************************************************************************")
print("根据您填写的信息，计算结果如下：")
print(f"""姓名：{name}
性别：{gender}
年龄：{age}
身高：{height}cm
体重：{weight}kg
基础代谢：{format_kcal(round(bmr,2))}
日常消耗：{format_kcal(round(daily_use,2))}
目的：{get_aim_str(aim)}
每日应摄入:{get_limit(aim)}{format_kcal(round(daily_eat,2))}（碳水={get_limit(aim)}{format_g(int(daily_eat * 0.5 / 4))}、蛋白质={get_limit(aim)}{format_g(int(daily_eat * 0.2 / 4))}、脂肪={format_g(int(daily_eat * 0.3 / 9))}）""")
print_tips()
input()
