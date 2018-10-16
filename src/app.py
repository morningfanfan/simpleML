import json

from flask import Flask, Response, abort, request
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from keras.backend import clear_session

import config
from model import MLModel
from util import check_data_format, check_idx_format
import error

app = Flask(__name__)
engine = create_engine(config.DATABASE_URI)

DEFAULT_MODEL_NAME = "stockdemo"


@app.route("/results")
def get_existed_results():
    try:
        model_name = request.args.get("model", DEFAULT_MODEL_NAME, type=str)
        idx = request.args.get("index")
        check_idx_format(idx)
        table_name = model_name
        text_sql = "SELECT output FROM " + \
            table_name + " WHERE id = " + str(idx) + ";"

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


@app.route("/predict", methods=["POST"])
def realtime_predict():
    model_name = request.json.get("model", DEFAULT_MODEL_NAME)
    data = request.json.get("data")

    try:
        check_data_format(data)
        clear_session()
        model_info = config.MODEL_LIST[model_name]
        model = MLModel(**model_info)
        res = model.predict(data)

        return Response(
            json.dumps({"output": res}),
            status=200,
            mimetype="application/json"
        )
    except IndexError as e:
        print(e)
        return abort(400, description=" not a valid data format")
    except KeyError as e:
        print(e)
        return abort(404, description="not a valid model name")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
