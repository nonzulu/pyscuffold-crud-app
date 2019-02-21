import json
class StudentDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as  json_file:
            self.__data = json.load(json_file)


    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student 

    def close(self):
        pass

    def calc_sum(a,b):
        return a + b

    def multiply(a,b):
        return a * b

    def division(a,b):
        return a / b

    def minus(a,b):
        return a - b

    def string(greet):
        return "hello world"
