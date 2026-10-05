class Student:
    def __init__(self, name, gender,tel,age,info):
        self.gender = gender
        self.tel = tel
        self.name = name
        self.age = age
        self.info = info

    def __str__(self):
        '''
        重写__str__方法，方便将学生对象，转换为字符串，写入文件
        '''
        return f'{self.name}，{self.gender}，{self.tel}，{self.age}，{self.info}'

    @staticmethod
    def generate(stu_str:str):
        '''
        从字符串中生成学生对象
        '''
        arr = stu_str.split(',')
        return Student(arr[0],arr[1],arr[2],arr[3],arr[4])


class Student_MS:
    def __init__(self,path,encoding):
        self.stu_dict = {}
        self.fr = open(path,'r',encoding=encoding)
        for line in self.fr.readlines():
            line = line.strip()
            stu = Student.generate(line)
            self.stu_dict[stu.name] = stu
        print(f"成功加载{len(self.stu_dict)}条学生数据")
        self.fw = open(path,'w',encoding=encoding)

    def add(self,stu:Student):
        '''
        添加学生
        :param stu: 学生对象
        '''
        print("准备添加学生，请依序填入学生信息：姓名，性别，手机号，年龄，信息")
        name = input("请输入姓名：")
        if name in self.stu_dict:
            print(f"姓名为{name}的学生已存在")
            is_continue = input("是否继续添加？(y/n)")
            if is_continue.lower() != 'y':
                print("添加已取消")
                return
        gender = input("请输入性别：")
        tel = input("请输入手机号：")
        age = input("请输入年龄：")
        info = input("请输入信息：")
        stu = Student(name,gender,tel,age,info)
        self.stu_dict[name] = stu
        print(f"成功添加学生：{stu}")

    def modify(self,stu:Student):
        '''
        修改学生信息
        :param stu: 学生对象
        '''
        name = input("请输入要修改的学生姓名：")
        if name not in self.stu_dict:
            print(f"姓名为{name}的学生不存在")
            return
        stu = self.stu_dict[name]
        print(f"当前学生信息：{stu}")
        print("准备修改学生信息，请依序填入学生信息：姓名，性别，手机号，年龄，信息")
        gender = input("请输入性别：")
        tel = input("请输入手机号：")
        age = input("请输入年龄：")
        info = input("请输入信息：")
        stu = Student(name,gender,tel,age,info)
        self.stu_dict[name] = stu
        print(f"成功修改学生：{stu}")

    def delete(self,stu:Student):
        '''
        删除学生
        :param stu: 学生对象
        '''
        name = input("请输入要删除的学生姓名：")
        if name not in self.stu_dict:
            print(f"姓名为{name}的学生不存在")
            return
        del self.stu_dict[name]
        print(f"成功删除学生：{stu}")

    def query(self,stu:Student):
        '''
        查询学生信息
        :param stu: 学生对象
        '''
        name = input("请输入要查询的学生姓名：")
        if name not in self.stu_dict:
            print(f"姓名为{name}的学生不存在")
            return
        stu = self.stu_dict[name]
        print(f"查询到的学生信息：姓名：{stu.name}，性别：{stu.gender}，手机号：{stu.tel}，年龄：{stu.age}，信息：{stu.info}")

    def show(self,stu:Student):
        '''
        显示所有学生信息
        :param stu: 学生对象
        '''
        for stu in self.stu_dict.values():
            print(f"姓名：{stu.name}，性别：{stu.gender}，手机号：{stu.tel}，年龄：{stu.age}，信息：{stu.info}")

    def save(self,stu:Student):
        '''
        保存学生数据到文件
        :param stu: 学生对象
        '''
        for stu in self.stu_dict.values():
            self.fw.write(f"{stu}\n")
        self.fw.close()
        print("成功保存学生数据到文件")

    @staticmethod
    def print_menu():
        '''
        打印菜单
        '''
        print("欢迎使用学生管理系统")
        print("-----------------")
        print("请选择要进行的操作：")
        print("1. 添加学生")
        print("2. 修改学生信息")
        print("3. 删除学生")
        print("4. 查询学生信息")
        print("5. 显示所有学生信息")
        print("6. 保存学生数据到文件")
        print("0. 退出系统")
        print("-----------------")

        return input("请输入您的选择：")


sms = Student_MS(r"E:\student.txt",'utf-8')
while True:
    choice = sms.print_menu()
    if choice == '0':
        print("谢谢使用")
        break
    elif choice == '1':
        sms.add(None)
        print()
    elif choice == '2':
        sms.modify(None)
        print()
    elif choice == '3':
        sms.delete(None)
        print()
    elif choice == '4':
        sms.query(None)
        print()
    elif choice == '5':
        sms.show(None)
        print()
    elif choice == '6':
        sms.save(None)
        print()
    else:
        print("输入错误，请重新输入")
        print()




















