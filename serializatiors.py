from dbs import Teacher, Mark


def serialize_teacherdata(teacher: Teacher):
    return {
        'id': teacher.id,
        'name': teacher.name,
        'age': teacher.age,
        'work_exp': teacher.work_exp,
        'subject': teacher.subject,
        'rating': teacher.rating,
        'personality': teacher.personality
    }


def serialize_markdata(mark: Mark):
    return {
        'id': mark.id,
        'teacher': mark.teacher.id,
        'student': mark.student,
        'value': mark.value,
        'timestamp': mark.timestamp
    }


def serialize_teacherNmark(teacher: Teacher):
    return {
        'a_teacher':serialize_teacherdata(teacher),
        'marks': len([serialize_markdata(mark) for mark in teacher.marks])
    }