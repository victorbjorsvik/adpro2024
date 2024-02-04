from pydantic import BaseModel
from pydantic import EmailStr  # Predefined validator
from pydantic import Field # To add default values
from pydantic import field_validator # for custom validations


class Person(BaseModel):
    """
    Class to describe a person.
    This is the docstring.
    If you shift+Tab in the notebook you can check this out
    """
    name: str
    course: str = Field(default="Business Analytics") #Default value
    email: EmailStr
    age: int

    @field_validator("age")
    def validate_age(cls, value):
        if value <= 0:
            raise ValueError(f"Age must be positive: {value}")
        return value

    # We use super() as a way of inherit all the variables from the pydantic Base Model
    # The primary purpose of super() is to support cooperative multiple inheritance.
    # When a class inherits from multiple parent classes, super() helps in resolving the order in which
    # the parent classes are called, ensuring that each class in the hierarchy is initialized properly. .
    # If you already defined a Model with pydantic and then defined the variable names,
    # then you can get them all into the instace, with the same order
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Methods are defined as usual
    def whoami(self):
        """Prints my id"""
        print(f"My name is {self.name} and I am {self.age} years old. I study {self.course}.")

if __name__ == "__main__":
    person = Person(name='Alex', email="alex@gmail.com", age=21)
    person.whoami()
