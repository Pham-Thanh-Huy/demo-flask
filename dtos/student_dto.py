from models.student import Student as student

class StudentDTO:
    def __init__(self, name, birth_date, gender, class_name):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name

    @classmethod
    def from_model(cls, student) -> 'StudentDTO':
        return cls(
            name = student.name,
            birth_date = student.birth_date,
            gender = student.gender,
            class_name= student.class_name
        )

    def to_dict(self) -> dict:
        return {
            "name" : self.name,
            "birth_date" : self.birth_date,
            "gender" : self.gender,
            "class_name" :self.class_name
        }