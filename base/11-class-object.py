class Student(object):

    # # 方法的第一个参数永远是self，表示创建的实例本身
    # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
    # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

if __name__ == "__main__":
    stu1 = Student('lilong', 98)
    stu1.print_score()
    print(stu1.get_grade())