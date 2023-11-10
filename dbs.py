import logging
from datetime import datetime

from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField, SmallIntegerField, FloatField


# logger = logging.getLogger('peewee')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

db = SqliteDatabase('sqlite3.db')

class BaseModel(Model):
    class Meta:
        database = db


class Teacher(BaseModel):
    name = CharField()
    age = SmallIntegerField()
    work_exp = SmallIntegerField()
    subject = CharField()
    rating = FloatField()
    personality = CharField()
    


class Mark(BaseModel):
    teacher = ForeignKeyField(Teacher, backref='marks')
    student = SmallIntegerField()
    value = IntegerField()
    timestamp = DateTimeField(default=datetime.now)

if __name__ == "__main__":
    db.connect()
    db.create_tables([Teacher, Mark])
    db.close()

# teacher_table = Teacher.select().execute()
# print(*[(ob.id,ob.name,ob.age,ob.work_exp,ob.subject,ob.rating,ob.personality) for ob in teacher_table],sep='\n')
# mark_table = Mark.select().execute()
# print(*[(ob.id,ob.teacher.name,ob.student,ob.value) for ob in mark_table],sep='\n')
