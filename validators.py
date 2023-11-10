from dbs import Teacher


class ValidationError(Exception):
    pass


def validate_teacherdata(data):
    name = data.get('name')
    age = data.get('age')
    work_exp = data.get('work_exp')
    subject = data.get('subject')
    rating = data.get('rating')
    personality = data.get('personality')

    if (not name and not age) or (not name or not age):
        raise ValidationError('name and age are required')

    if not isinstance(age, int):
        raise ValidationError('age must be integer')
    if not isinstance(name, str):
        raise ValidationError('name must be string')
    if work_exp and not isinstance(work_exp, int):
        raise ValidationError('work_exp must be integer')
    if subject and not isinstance(subject, str):
        raise ValidationError('subject must be string')
    if rating and not isinstance(rating, float):
        raise ValidationError('rating must be float')
    if personality and not isinstance(personality, str):
        raise ValidationError('personality must be string')

    if age < 0:
        raise ValidationError('age must be positive')
    if name == '':
        raise ValidationError('name must not be empty')


def validate_markdata(data):
    teacher_id = data.get('teacher_id')
    student = data.get('student')
    value = data.get('value')

    teacher = Teacher.get_or_none(id=teacher_id)

    if not teacher:
        raise ValidationError('teacher with such id does not exist')

    if not (teacher_id and value and student):
        raise ValidationError('teacher_id, value and student are required')

    if not isinstance(teacher_id, int):
        raise ValidationError('teacher_id must be integer')
    if not isinstance(student, int):
        raise ValidationError('student must be integer')
    if not isinstance(value, int):
        raise ValidationError('value must be integer')

    if value < 0:
        raise ValidationError('value must be positive')
    if student < 1:
        raise ValidationError('there are no negative students!')

    data['teacher'] = teacher
    return data

def validate_teacherpatch(data):
    name = data.get('name')
    age = data.get('age')
    work_exp = data.get('work_exp')
    subject = data.get('subject')
    rating = data.get('rating')
    personality = data.get('personality')
    
    if age and not isinstance(age, int):
        raise ValidationError('age must be integer')
    if name and not isinstance(name, str):
        raise ValidationError('name must be string')
    if work_exp and not isinstance(work_exp, int):
        raise ValidationError('work_exp must be integer')
    if subject and not isinstance(subject, str):
        raise ValidationError('subject must be string')
    if rating and not isinstance(rating, float):
        raise ValidationError('rating must be float')
    if personality and not isinstance(personality, str):
        raise ValidationError('personality must be string')

    if age and age < 0:
        raise ValidationError('age must be positive')
    if name and name == '':
        raise ValidationError('name must not be empty')
    
