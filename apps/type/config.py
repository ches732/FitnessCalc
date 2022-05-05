from pydantic import BaseModel, ValidationError, validator
from type.gender import GenderType


category_male = ["male", "guy", "men"]
category_children_boy = ["boy", "youth"]
category_female = ["female", "woman"]
category_children_girl = ["girl", "young girl"]
metabolism = {"Short": 1.2, "Average": 1.375, "High": 1.55, "Extreme": 1.7}


class Parameters(BaseModel):
    gender: str
    weight: float
    height: float
    age: float
    exercise_stress: str

    @validator("gender")
    def gender_valid(cls, v):
        """Checking the incoming parameter, followed by processing"""
        if v in category_male:
            v = GenderType.MALE
        elif v in category_female:
            v = GenderType.FEMALE
        elif v in category_children_girl:
            v = GenderType.CHILDRENGIRL
        elif v in category_children_boy:
            v = GenderType.CHILDRENBOY
        else:
            raise ValidationError("Wrong gender entered")
        return v

    @validator("exercise_stress")
    def exercise_stress_valid(cls, e):
        """Checking the incoming parameter, followed by processing"""
        if e in metabolism:
            return e
        else:
            e = "Short"
        return e