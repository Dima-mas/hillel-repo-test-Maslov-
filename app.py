from flask import Flask, jsonify, request
from peewee import fn

from dbs import Teacher, Mark
from deserializators import deserialize_teacherdata, deserialize_markdata,deserialize_teacherpatch
from serializatiors import serialize_teacherdata, serialize_markdata, serialize_teacherNmark
from validators import validate_teacherdata, validate_markdata, validate_teacherpatch, ValidationError
from test_server import test_teacher_update

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'message': 'The start'})


@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify({'message': str(error)})
    response.status_code = 422

    return response


@app.route('/teachers', methods=['GET', 'POST'])
def teachers_api():
    if request.method == 'GET':

        filter_name = request.args.get('name')
        filter_age = request.args.get('age')
        filter_personality = request.args.get('pers')

        teachers = Teacher.select(Teacher, fn.AVG(Mark.value).alias('Average_student_mark')).join(Mark).group_by(Teacher).order_by(
            fn.AVG(Mark.value).desc())

        if filter_name:
            teachers = teachers.where(Teacher.name.contains(filter_name))
        if filter_age:
            teachers = teachers.where(Teacher.age == filter_age)
        if filter_personality:
            teachers = teachers.where(Teacher.personality == filter_personality)

        return jsonify([serialize_teacherdata(teacher) for teacher in teachers])

    elif request.method == 'POST':

        data = deserialize_teacherdata()
        validate_teacherdata(data)

        teacher = Teacher.create(**data)

        return jsonify(serialize_teacherdata(teacher)), 201


@app.route('/teachers/<int:teacher_id>', methods=['GET','PATCH','DELETE'])
def teacher_api(teacher_id):
    if request.method == 'GET':
        teacher = Teacher.get_or_none(id=teacher_id)
        if not teacher:
            return jsonify({'message': 'teacher not found'}), 404

        return jsonify(serialize_teacherNmark(teacher))
    
    elif request.method == 'PATCH':
        
        data = deserialize_teacherpatch()
        validate_teacherpatch(data)
        teacher = Teacher.update(**data).where(Teacher.id == teacher_id).execute()
        
        teacher = Teacher.get_or_none(id=teacher_id)
        if not teacher:
            return jsonify({'message': 'teacher not found'}), 404
        return jsonify(serialize_teacherdata(teacher)), 201

    elif request.method == 'DELETE':
        teacher = Teacher.get_or_none(id=teacher_id)
        if not teacher:
            return jsonify({"message": "record not found"}), 404
        deletion = Teacher.delete().where(Teacher.id == teacher_id).execute()
        return jsonify({'record':serialize_teacherNmark(teacher),'status':'deleted'})

@app.route('/marks', methods=['GET'])
def marks_api():
    if request.method == 'GET':

        marks = Mark.select(Mark, Teacher.id).join(Teacher)
        return jsonify([serialize_markdata(mark) for mark in marks])

@app.route('/marks/<int:teacher_id>', methods=['GET', 'POST'])
def mark_api(teacher_id):
    if request.method == 'POST':
        
        data = deserialize_markdata()
        validated_data = validate_markdata(data)
        # validated_data['student'] = student

        mark = Mark.create(**validated_data)
        # mark.student = student

        return jsonify(serialize_markdata(mark)), 201

    if request.method == 'GET':
        teacher = Teacher.get_or_none(id=teacher_id)
        if not teacher:
            return jsonify({'message': 'teacher not found'}), 404

        marks = Mark.select(Mark, Teacher).join(Teacher).where(Teacher.id == teacher_id)
        return jsonify([serialize_markdata(mark) for mark in marks])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)