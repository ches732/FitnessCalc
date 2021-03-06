from flask import Flask, jsonify, abort, request
from module.calcs.base import BaseFitnessCalc
from module.calcs.parents import FemaleFitnessCalc, MaleFitnessCalc
from type.config import Parameters, ValidationError
from type.gender import GenderType
from module.calcs.database import Database

app = Flask(__name__)

db = Database()


@app.route('/calc/api/v1.0/bju', methods=['POST'])
def counting_bju():
    try:
        parameters = Parameters(**request.json)
        req_bju_json = parameters
    except ValidationError:
        print("You must enter the correct parameter")
        abort(400)
    else:
        base = BaseFitnessCalc(
            gender=GenderType(req_bju_json.gender), weight=req_bju_json.weight, height=req_bju_json.height,
            age=req_bju_json.age, exercise_stress=req_bju_json.exercise_stress
        )
        result_bju = base.squirrels_fatscarbohy_drates()
        db.write_data_to_table_result(
            ip_adress=request.remote_addr, gender=GenderType(req_bju_json.gender).value, bju=result_bju, cursor=None
        )
        return jsonify({"result_bju": result_bju})


@app.route('/calc/api/v1.0/water', methods=['POST'])
def counting_water():
    try:
        parameters = Parameters(**request.json)
        req_water_json = parameters
    except ValidationError:
        print("You must enter the correct parameter")
        abort(400)
    else:
        base = BaseFitnessCalc(
            gender=GenderType(req_water_json.gender), weight=req_water_json.weight, height=req_water_json.height,
            age=req_water_json.age, exercise_stress=req_water_json.exercise_stress
        )
        result_water = base.water()
        db.write_data_to_table_result(
            ip_adress=request.remote_addr, gender=GenderType(req_water_json.gender).value, water=result_water,
            cursor=None
        )
        return jsonify({"result_water": result_water})


@app.route('/calc/api/v1.0/callories', methods=['POST'])
def counting_callories():
    try:
        parameters = Parameters(**request.json)
        req_callories_json = parameters
    except ValidationError:
        print("You must enter the correct parameter")
        abort(400)
    else:
        if req_callories_json.gender is GenderType.MALE:
            calc = MaleFitnessCalc(
                weight=req_callories_json.weight, height=req_callories_json.height, age=req_callories_json.age,
                exercise_stress=req_callories_json.exercise_stress
            )
            result_sfd = calc.squirrels_fatscarbohy_drates()
            result_callories = calc.calc_calories()
            db.write_data_to_table_result(
                ip_adress=request.remote_addr, gender=GenderType(req_callories_json.gender).value,
                callories=result_callories, cursor=None
            )
        else:
            calc = FemaleFitnessCalc(
                weight=req_callories_json.weight, height=req_callories_json.height, age=req_callories_json.age,
                exercise_stress=req_callories_json.exercise_stress
            )
            result_sfd = calc.squirrels_fatscarbohy_drates()
            result_callories = calc.calc_calories()
            db.write_data_to_table_result(
                ip_adress=request.remote_addr, gender=GenderType(req_callories_json.gender).value,
                callories=result_callories, cursor=None
            )
        return jsonify({"result_callories": result_callories})


@app.route('/calc/api/v1.0/param', methods=['GET'])
def param():
    response = db.getting_results()
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
