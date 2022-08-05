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
        self.load_student_file()
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
                self.student_save_file()
            elif num == 7:
                # 退出
                break

    def load_student(self):
        """
        从文件中加载学员 利用pandas
        """
        # 如果该路径下存在Excel，则进行读取；如果不存在则进行创建
        try:
            df = pd.read_excel('G:/Python/学员信息.xlsx', names=None)
            data_from_excel = df.to_dict(orient='records')
            # 列表推导式=>创建一个新的列表，遍历data_from_excel并将Student实例化对象赋值给student_list
            self.student_list = [Student(num=i['num'], name=i['name'], age=[i['age']]) for i in data_from_excel]
            # print(data_from_excel)
            # print(self.student_list)
        except:
            df = pd.DataFrame(columns=['name', 'num', 'age'])
            df.set_index('num', inplace=True)
            df.to_excel('G:/Python/学员信息.xlsx')

    @staticmethod
    def show_main():
        print("请选择您要执行的功能选项：")
        print("1：新增学员")
        print("2：查询学员")
        print("3：删除学员")
        print("4：修改学员")
        print("5：显示所有")
        print("6：保存学员")
        print("7：退出系统")

    def student_add(self):
        num = input('请输入学员学号：')
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')

        students = Student(num, name, age)
        self.student_list.append(students)
        self.student_show_all()

    def student_search(self):
        name = input('请输入需要查看学生姓名：')

        for student in self.student_list:
            if student.name == name:
                print(student)
                # 查到了之后跳出循环
                break
        else:
            print("查无此人")

    def student_delete(self):
        name = input('请输入需要删除学生姓名：')

        for student in self.student_list:
            if student.name == name:
                self.student_list.remove(student)
        else:
            print('该学员不存在')
        self.student_show_all()

    def student_update(self):
        name = input('请输入需要修改学生姓名：')

        for student in self.student_list:
            if student.name == name:
                student.name = input('请输入修改后的名字：')
                student.num = input('请输入修改后的学号：')
                student.tel = input('请输入修改后的年龄：')
                print(f'修改成功，修改后学员姓名为{student.name},学号是{student.num},年龄是{student.age}')
                # 修改了之后跳出循环
                break
        else:
            print('该学员不存在')

        self.student_show_all()

    def student_show_all(self):
        """
        显示所有学生
        """
        print('姓名\t学号\t年龄')
        for s in self.student_list:
            print(f'{s.name}\t{s.num}\t{s.age}')

    def student_save(self):
        """
        保存数据到EXCEL(with pandas)
        """
        names = [i.name for i in self.student_list]
        ages = []
        nums = []
        for student_data in self.student_list:
            nums.append(student_data.num)
            ages.append(student_data.age)
        df = pd.DataFrame({"name": names, "num": nums, "age": ages})
        print(df)
        # df.set_index("num", inplace=True)
        # df.to_excel("G:/Python/学员信息.xlsx")

    def load_student_file(self):
        try:
            # 打开文件
            f = open('student.data', 'r')
        except:
            # 该文件不存在，进行w模式的创建
            # w:写入模式，如果不存在则进行创建，如果存在进行清空重写
            f = open('student.data', 'w')
        else:
            # else语句，当执行try之后才执行else，执行except语句不会执行else
            # 文件打开之后进行读取
            data = f.read()
            # 读取的data数据是str类型，使用eval函数转换成字典类型数据
            new_list = eval(data)
            # 列表推导式创建学生列表
            self.student_list = [Student(i['num'], i['name'], i['age']) for i in new_list]
        finally:
            # 关闭文件
            f.close()

    def student_save_file(self):
        # 打开文件
        f = open('student.data', 'w')
        # 遍历学生数据对象并获取字典数据
        newfile = [i.__dict__ for i in self.student_list]
        # 写入文件对象，write()参数类型为str类型
        f.write(str(newfile))
        # 关闭文件对象
        f.close()
