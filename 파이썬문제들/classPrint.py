class Member:
    def __init(self, name, type, grade):
        self.name = name
        self.type = type
        self.grade = grade

    def set_grade(self, set_grade):
        self.grade = set_grade

    def get_type(self, input_type):
        self.type = input_type()

    def get_grade(self, get_grade):
        self.grade = get_grade


class Person(Member):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return print(self.name + ' ' + self.type + ' ' + '준회원')


#  child class of Member:  Group
class Group(Member):
    def __init__(self, name, type, grade):
        self.name = name
        self.type = type
        self.grade = grade

    def set_ceo(self, ceo):
        self.ceo = ceo

    def get_ceo(self, ceo):
        print('대표자:' + self.ceo)

    def __str__(self):
        return print(self.grade + ' ' + self.name + ' ' + self.type + ' ' + '정회원')


result = []

# loop 3 times
for i in range(0, 3):
    type = int(input('회원 구분(1:개인, 2:단체):'))

    if type == 1:
        name = input('성명 입력:')
        type = '개인'
        person = Person(name, type)
        result.append(person)

    elif type == 2:
        grade = input('상호명 입력:')
        name = input('대표이사명 입력:')
        type = '단체'
        group = Group(name, type, grade)
        result.append(group)

for i in range(0, 3):
    result[i].__str__()
