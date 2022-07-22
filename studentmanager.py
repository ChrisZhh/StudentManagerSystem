from student import Student
import pandas as pd


class StudentManager(object):
    """
    学生管理
    """

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
        从文件中加载学员 利用pandas
        """
        df = pd.read_excel('G:/Python/学员信息.xlsx', names=None)
        data_from_excel = df.values.tolist()
        for data in data_from_excel:
            self.student_list.append(data)

        # students = Student(153020198, '李渊大', 25)
        # self.student_list.append(students.__str__())
        # print(self.student_list)

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
        num = input('请输入学员学号：')
        name = input('请输入学生姓名：')
        tel = input('请输入学生电话：')

        students = Student(num, name, tel)
        self.student_list.append(students)

    def student_search(self):
        name = input('请输入需要查看学生姓名：')

        for student in self.student_list:
            if student.name == name:
                print(student)

    def student_delete(self):
        name = input('请输入需要删除学生姓名：')

        for student in self.student_list:
            if student.name == name:
                self.student_list.remove(student)

    def student_update(self):
        name = input('请输入需要修改学生姓名：')

        for student in self.student_list:
            if student.name == name:
                new_name = input('请输入修改后的名字：')
                new_num = input('请输入修改后的学号：')
                new_tel = input('请输入修改后的电话：')

                student.name = new_name
                student.num = new_num
                student.tel = new_tel

    def student_show_all(self):
        for student in self.student_list:
            print(student)

    def student_save(self):
        df = pd.DataFrame(self.student_list)
        print(df)
