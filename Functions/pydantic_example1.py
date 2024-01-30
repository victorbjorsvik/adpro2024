from pydantic import BaseModel


class Person(BaseModel):
    name: str
    course: str
    age: int


person = Person(name=5, course="Business", age=21)
