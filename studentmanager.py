from student import Student


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()

    def load_student(self):
        students = Student('aa', '男', 21)
        self.student_list.append(students)

    def show_main(self):
        self.load_student()
        while True:
            num = input('请选择具体操作：\n'
                        '1：新增\n'
                        '2：查询\n'
                        '3：删除\n'
                        '4：更新\n'
                        '5：退出\n')
            if int(num) == 1:
                self.student_add()
            elif int(num) == 2:
                self.student_search()
            elif int(num) == 3:
                self.student_delete()
            elif int(num) == 4:
                self.student_update()
            else:
                break

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
