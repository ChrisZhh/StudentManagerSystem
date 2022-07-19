from student import Student


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        # 1.加载学员
        self.load_student()
        while True:
            # 2.加载菜单
            self.show_main()
            # 3.接收输入执行对应功能选项
            num = int(input('请选择具体操作：'))
            if num == 1:
                # 增
                self.student_add()
            elif num == 2:
                # 查
                self.student_search()
            elif num == 3:
                # 删
                self.student_delete()
            elif num == 4:
                # 改
                self.student_update()
            elif num == 5:
                # 显示所有
                self.student_show_all()
            elif num == 6:
                # 存
                self.student_save()
            elif num == 7:
                # 退出
                break

    def load_student(self):
        """
        从文件中加载学员
        """
        students = Student('aa', '男', 21)
        self.student_list.append(students)

    @staticmethod
    def show_main():
        print("请选择您要执行的功能选项：")
        print("1：新增学员")
        print("2：查询学员")
        print("3：删除学员")
        print("4：修改学员")
        print("5：显示所有")
        print("6：保存学员")
        print("6：退出系统")

    def student_add(self):
        students = Student('bb', '女', 21)
        self.student_list.append(students)

    def student_search(self):
        for student in self.student_list:
            print(student)

    def student_delete(self):
        for student in self.student_list:
            if student.name == 'aa':
                self.student_list.remove(student)

    def student_update(self):
        for student in self.student_list:
            if student.name == 'bb':
                student.tel = 31
                student.gender = '男'
