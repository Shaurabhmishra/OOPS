###### Class Blueprint ######

class Student:
    # class developed for demo purpose
    '''Sample statement for __doc__ string'''
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
    
    def talk(self):
        print("Hello My name is ", self.name)
        print("My Roll number is ", self.rollno)


# refrence variable name = object name of class
s = Student(100, 'Sunny')           
print(s.name)

print(s.rollno)
s.talk()

s1 = Student(200, 'Bunny')          #### object name 2
s1.talk()

print(Student.__doc__)              #### dictionary for instance variable (if defined)
# print(help(Student))

print(id(s))                        #### To know the address