from flask import request

def deserialize_teacherdata():
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')
    work_exp = data.get('work_exp')
    subject = data.get('subject')
    rating = data.get('rating')
    personality = data.get('personality')
    return {
        'name': name,
        'age': age,
        'work_exp': work_exp,
        'subject': subject,
        'rating': rating,
        'personality': personality
        
    }


def deserialize_markdata():
    data = request.get_json()
    
    teacher_id = data.get('teacher_id')
    student = data.get('student')
    value = data.get('value')
    timestamp = data.get('timestamp')

    return {
        'teacher_id': teacher_id,
        'student': student,
        'value': value,
        'timestamp': timestamp
   }

def deserialize_teacherpatch():
    data = request.get_json()

    patch_req = {'name': data.get('name'),
        'age': data.get('age'),
        'work_exp': data.get('work_exp'),
        'subject': data.get('subject'),
        'rating': data.get('rating'),
        'personality': data.get('personality')}
    
    
    update_dict = {}
    for key,value in patch_req.items():
        if value or type(value)==int:
            update_dict.update({key:value})
    return update_dict
