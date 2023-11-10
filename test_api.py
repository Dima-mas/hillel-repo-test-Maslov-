from unittest import TestCase
from app import app


class TestApi(TestCase):
    def setUp(self) -> None:
        # set up flast test client
        self.client = app.test_client()

    def test_api_get_teachers(self):
        # send request to /teachers
        response = self.client.get("/teachers")

        # check status code
        self.assertEqual(response.status_code, 200)

    def test_api_get_marks(self):
        # send request to /teachers
        response = self.client.get("/marks")

        # check status code
        self.assertEqual(response.status_code, 200)

    def test_api_create_teacher_negative_age(self):
        # send request to /teachers
        response = self.client.post("/teachers", json={
            "name": "Nataliia",
            "age": -1,
            'work_exp':5999,
            'subject':'Someology',
            'rating':99.9,
            'personality':'Random'
        })

        # check status code
        self.assertEqual(response.status_code, 422)

    def test_api_create_teacher_no_data(self):
        # send request to /teachers
        response = self.client.post("/teachers", json={
        })

        # check status code
        self.assertEqual(response.status_code, 422)

    def test_api_create_teacher(self):
        # send request to /teachers
        response = self.client.post("/teachers", json={
            "name": "Nataliia",
            "age": 6000,
            'work_exp':5999,
            'subject':'Someology',
            'rating':99.9,
            'personality':'Random'
        })

        # check status code
        self.assertEqual(response.status_code, 201)
ob = TestApi()
ob.setUp()
ob.test_api_create_teacher()
ob.test_api_create_teacher_negative_age()
ob.test_api_create_teacher_no_data()
ob.test_api_get_marks()
ob.test_api_get_teachers()
print('ok')
