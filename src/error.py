from flask import jsonify
from app import app


@app.errorhandler(404)
def custom404(description="404 not found"):
    response = jsonify({'message': description})
    response.status_code = 404
    return response


@app.errorhandler(400)
def custom400(description="400 bad request"):
    response = jsonify({'message': description})
    response.status_code = 400
    return response
