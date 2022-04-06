from typing import Union
from module.calcs.Base import BaseFitnessCalc
from type.gender import GenderType


class ChildrenBoyFitnessCalc(BaseFitnessCalc):

    def __init__(self, weight: float, height: float, age: float, exercise_stress: str):
        super().__init__(weight, height, age, GenderType.CHILDRENBOY, exercise_stress)

    def calc_calories(self) -> Union[float, None]:
        """Daily Calorie Calculation."""
        self.result_calories_male = self.result * self.metabolism[self.exercise_stress]
        return self.result_calories_male


class ChildrenGirlFitnessCalc(BaseFitnessCalc):

    def __init__(self, weight: float, height: float, age: float, exercise_stress: str):
        super().__init__(weight, height, age, GenderType.CHILDRENGIRL, exercise_stress)

    def calc_calories(self) -> Union[float, None]:
        """Daily Calorie Calculation."""
        self.result_calories_female = self.result * self.metabolism[self.exercise_stress]
        return self.result_calories_female