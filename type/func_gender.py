from module.Parents import MaleFitnessCalc, FemaleFitnessCalc
from module.Children import ChildrenBoyFitnessCalc, ChildrenGirlFitnessCalc


category_male = ["male", "guy", "men"]
category_children_boy = ["girl", "young girl"]
category_female = ["female", "woman", "girl"]
category_children_girl = ["boy", "youth"]
metabolism = {"Short": 1.2, "Average": 1.375, "High": 1.55, "Extreme": 1.7}

if __name__ == "__main__":
    gender = input("Enter gender:")
    weight = float(input("Enter weight:"))
    height = float(input("Enter height:"))
    age = float(input("Enter age:"))
    print("You must select an option:\n"
          "Short - is sedentary work in the office and lack of sports\n"
          "Average - Mobile work and / or classes in the gym 1 - 3 times a week\n"
          "High - Regular strength and cardio train coefficient ing at least three times a week\n"
          "Extreme - Preparation for competitions, hard training 5 or more times a week\n")
    exercise_stress = input("Enter option:")

    if exercise_stress not in metabolism:
        exercise_stress = "Short"
    if gender in category_male:
        calc = MaleFitnessCalc(weight, height, age, exercise_stress)
    elif gender in category_female:
        calc = FemaleFitnessCalc(weight, height, age, exercise_stress)
    elif gender in category_children_boy:
        calc = ChildrenBoyFitnessCalc(weight, height, age, exercise_stress)
    elif gender in category_children_girl:
        calc = ChildrenGirlFitnessCalc(weight, height, age, exercise_stress)
    else:
        raise Exception("idi nahui")

    print("Daily rate of BJU:", calc.squirrels_fatscarbohy_drates())
    print("Daily calorie intake:", calc.calc_calories())
    print("Daily rate of water:", calc.water())
