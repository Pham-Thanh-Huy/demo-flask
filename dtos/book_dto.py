class BookDTO:
    def __init__(self, id: int, name: str, page_count: int, student_id: int):
        self.id = id
        self.name = name
        self.page_count = page_count
        self.student_id = student_id

    @staticmethod
    def from_model(book):
        return BookDTO(
            id=book.id,
            name=book.name,
            page_count=book.page_count,
            student_id=book.student_id
        )

    def to_dict(self):
        return self.__dict__