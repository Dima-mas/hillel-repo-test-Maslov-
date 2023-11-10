from peewee import fn
from random import randint as ran

from dbs import Teacher, Mark

#insert teacher data
def insert_teacherdata():
    with open('Teacher_data.txt','r') as file:
        data_list = []
        for line in file.readlines():
            data_list.append(tuple(line.split()))
        Teacher.insert_many(data_list).execute()

#generate mark data
def gen_markdata():
    for i in range(1000):
        teacher = Teacher.select().order_by(fn.Random()).get()
        
        Mark.create(teacher=teacher,student=ran(1,90),value=ran(10,100))

insert_teacherdata()
gen_markdata()
