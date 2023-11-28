def student(id,name):
    print(id,name)
student(id = 67,name ='shanta')

#one * def function
def person(*details):
    #output is tuples
    print(details)
person('Shanta', 4.00, 'Oxford')


def add(*num):
    sum = 0
    for i in num:
        sum += i
    print(sum)

add(21,90)

#def with key value **
def student_details(**details):
    #output is dictionary
    print(details)
student_details(b_name = 'Shanta', g_name = 'Maisha')