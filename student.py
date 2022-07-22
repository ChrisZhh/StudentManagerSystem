class Student(object):
    """
    学生类
    """

    # 学生类：学号，姓名，电话
    def __init__(self, num, name, tel):
        self.num = num
        self.name = name
        self.tel = tel

    def __str__(self):
        return [self.num, f'{self.name}', self.tel]
