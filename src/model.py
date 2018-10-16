import numpy as np
from config import MODEL_LIST

"""
class for newing a machine learning model object
"""


class MLModel:
    def __init__(self, name):
        self.model = MODEL_LIST[name]

    def predict(self, data):
        X = np.asarray(data)
        if len(X.shape) == 1:
            X = X.reshape(1, -1)

        try:
            result, = self.model.predict(X)
            return float(result)
        except ValueError as e:
            print(e)
