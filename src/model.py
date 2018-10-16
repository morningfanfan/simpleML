import numpy as np
from keras.models import load_model


class MLModel:

    def __init__(self, name):
        self.model = load_model(name)
    
    def predict(self, data):
        try:
            result, = self.model.predict(np.asarray(data).reshape(1,4))
            return float(result[0])
        except ValueError as e:
            print(e)
