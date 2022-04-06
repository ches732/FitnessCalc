from pydantic import BaseModel, ValidationError, validator
from type.gender import GenderType

category_male = ["male", "guy", "men"]
category_children_boy = ["girl", "young girl"]
category_female = ["female", "woman", "girl"]
category_children_girl = ["boy", "youth"]
metabolism = {"Short": 1.2, "Average": 1.375, "High": 1.55, "Extreme": 1.7}


class Parameters(BaseModel):
    gender: str
    weight: float
    height: float
    age: float
    exercise_stress: str

    @validator("gender")
    def gender_valid(cls, v):
        if v in category_male:
            v = GenderType.MALE
        elif v in category_female:
            v = GenderType.FEMALE
        else:
            raise ValidationError("Wrong gender entered")
        return v

    @validator("exercise_stress")
    def exercise_stress_valid(cls, e):
        if e in metabolism:
            return e
        else:
            e = "Short"
        return e
