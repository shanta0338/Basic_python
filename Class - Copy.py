class Student:
    roll = ''
    name = ''
    address = ''
    college_name = ''
    def __init__(self, name, roll, address, college_name):
       self.name = name
       self.roll = roll
       self.address = address
       self.college_name = college_name

    """
    def set_value(self,roll,name,addesss,college_name):
       self.name = name
       self.roll = roll
       self.address = addesss
       self.college_name = college_name
       """
    def display(self):
     print(f'Roll:{self.roll}, Name:{self.name}, Address:{self.address}, College:{self.college_name}')
     
rakib = Student('shnata',1,'kaptai','karnafullty')
#rakib.set_value('rakib',21, 'kaptai','Wayen State University')
rakib.display()