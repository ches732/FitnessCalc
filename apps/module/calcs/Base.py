from typing import Union
from type.gender import GenderType


class BaseFitnessCalc:
    metabolism = {"Short": 1.2, "Average": 1.375, "High": 1.55, "Extreme": 1.7}

    def __init__(self, weight: float, height: float, age: float, gender: GenderType, exercise_stress: str) -> None:
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.exercise_stress = exercise_stress


    def squirrels_fatscarbohy_drates(self) -> Union[float, None]:
        """We calculate the daily intake of protein, fats and carbohydrates."""
        if self.gender is GenderType.MALE:
            self.result_sfd = 655.1 + (9.563 * self.weight) + (1.85 * self.height) - (1.85 * self.age)
        elif self.gender is GenderType.FEMALE:
            self.result_sfd = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age)
        elif self.gender is GenderType.CHILDRENGIRL:
            self.result_sfd = 33.25 + (6.875 * self.weight) + (2.501 * self.height) - (3.385 * self.age)
        elif self.gender is GenderType.CHILDRENBOY:
            self.result_sfd = 330.05 + (4.782 * self.weight) + (0.92 * self.height) - (0.92 * self.age)
        else:
            self.result_sfd = None
            print("Specify gender")
        return self.result_sfd

    def water(self) -> Union[float, None]:
        """We calculate the daily rate of water."""
        if self.gender is GenderType.MALE:
            self.result_water = self.weight * 31
        elif self.gender is GenderType.FEMALE:
            self.result_water = self.weight * 35
        elif self.gender is GenderType.CHILDRENGIRL:
            self.result_water = self.weight * 18
        elif self.gender is GenderType.CHILDRENBOY:
            self.result_water = self.weight * 16
        else:
            self.result_water = None
            print("Specify gender")
        return self.result_water