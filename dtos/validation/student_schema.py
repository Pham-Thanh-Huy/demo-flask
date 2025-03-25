from marshmallow import Schema, fields


class StudentSchema(Schema):
    name = fields.String(required=True, error_messages={"required" : "Tên không được để trống"})
    birth_date = fields.Date(required=True, error_messages={"required" : "Ngày sinh không được để trống"})
    gender = fields.String(required=True, error_messages={"required" : "Giới tính không được để trống"})
    class_name = fields.String(required=True, error_messages={"required" : "class_name không được để trống"})