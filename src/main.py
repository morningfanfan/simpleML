import json

import sklearn
from flask import Response, abort, request
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

import config
import error
from app import app
from model import MLModel
from util import check_data_format, check_idx_format


engine = create_engine(config.DATABASE_URI)  # init database

DEFAULT_MODEL_NAME = "stockdemo"


"""
URL: /results
METHOD: GET
PARAMETERS: 
          VALUE: model(default=stockdemo), index
          FORM: url param
FUNCTION: return the value of 'output' in the database of the specified model 
"""


@app.route("/results")
def get_existed_results():
    try:
        model_name = request.args.get("model", DEFAULT_MODEL_NAME, type=str)
        idx = request.args.get("index")
        check_idx_format(idx)
        table_name = model_name  # the table name is stored the same as the model name
        text_sql = "SELECT output FROM " + \
            table_name + " WHERE id = " + str(idx) + ";"  # raw SQL sentence
        with engine.connect() as con:
            res = con.execute(text(text_sql))
            output, = res

        return Response(
            json.dumps({"output": output["output"]}),
            status=200,
            mimetype="application/json"
        )
    except ValueError as e:
        print(e)
        return abort(404, description=" not a valid id")
    except OperationalError as e:
        print(e)
        message = e.args[0]
        if "no such table" in message:
            return abort(404, description=" not a valid model")
        else:
            raise


"""
URL: /predict
METHOD: POST
PARAMETERS: 
           VALUE:model(default=stockdemo), data
           FORM: raw json
FUNCTION: return the output of the specified model by using the offered data as an input
"""


@app.route("/predict", methods=["POST"])
def realtime_predict():
    model_name = request.json.get("model", DEFAULT_MODEL_NAME)
    data = request.json.get("data")

    try:
        check_data_format(data)
        model = MLModel(model_name)
        res = model.predict(data)

        return Response(
            json.dumps({"output": res}),
            status=200,
            mimetype="application/json"
        )
    except ValueError as e:
        print(e)
        return abort(400, description=" not a valid data format")
    except KeyError as e:
        print(e)
        return abort(404, description="not a valid model name")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
