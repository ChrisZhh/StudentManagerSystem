class Student(object):
    """
    学生类
    """
    # 学生类：姓名，性别，电话
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'
