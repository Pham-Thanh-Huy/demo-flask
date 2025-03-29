from marshmallow import Schema, fields, validate

class BookSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    page_count = fields.Int(required=True, validate=validate.Range(min=1))
    student_id = fields.Int(required=True)