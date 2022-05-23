from typing import Union
from module.calcs.base import BaseFitnessCalc
from type.gender import GenderType


class MaleFitnessCalc(BaseFitnessCalc):

    def __init__(self, weight: float, height: float, age: float, exercise_stress: str):
        super().__init__(weight, height, age, GenderType.MALE, exercise_stress)

    def calc_calories(self) -> Union[float, None]:
        """Daily Calorie Calculation."""
        self.result_calories_male = self.result_sfd * self.metabolism[self.exercise_stress]
        return self.result_calories_male


class FemaleFitnessCalc(BaseFitnessCalc):

    def __init__(self, weight: float, height: float, age: float, exercise_stress: str):
        super().__init__(weight, height, age, GenderType.FEMALE, exercise_stress)

    def calc_calories(self) -> Union[float, None]:
        """Daily Calorie Calculation."""
        self.result_calories_female = self.result_sfd * self.metabolism[self.exercise_stress]
        return self.result_calories_female
