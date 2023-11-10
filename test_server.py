import requests


def test_teacher_creation():
    name = "Nataliia"
    age = 25
    work_exp = 5

    request_json = {"name": name, "age": age,'work_exp':5}

    response = requests.post(
        "http://localhost:5004/teachers",
        json=request_json
    )
    print(response.status_code)
    print(response.json())

def test_teacher_update():
    age = 33

    request_json = {"age": age}

    response = requests.patch(
        "http://localhost:5004/teachers/1",
        json=request_json
    )
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    test_teacher_update()
    test_teacher_creation()
