from pydantic import BaseModel, ValidationError, validator
from type.func_gender import category_male, category_female, metabolism
from type.gender import GenderType


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
