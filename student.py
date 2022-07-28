class Student(object):
    """
    学生类
    """

    # 学生类：学号，姓名，电话
    def __init__(self, num, name, age):
        self.num = num
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.num}, {self.name}, {self.age}"
