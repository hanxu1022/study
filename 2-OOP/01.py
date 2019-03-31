
"""
定义一个学生类，用来形容个学生
"""
# 定义一个空的类
class Student():
    # 定义一个类时，类下面必须有东西
    # pass此时的作用就是占位，必须有，不然报错
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类， 用来描述听Python的学生
class PythonStudent():
    name = None # 不确定具体值时，用None占位
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进层级
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print("I 在做作业")

        # 在函数末尾使用return语句
        return None
# 实例化一个叫yueyue的学生， 是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()