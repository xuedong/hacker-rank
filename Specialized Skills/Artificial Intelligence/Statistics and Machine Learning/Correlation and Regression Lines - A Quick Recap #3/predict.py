#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    X = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3]).reshape(-1, 1)
    y = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15])

    model = LinearRegression().fit(X, y)
    prediction = model.predict(np.array([10]).reshape(-1, 1))[0]
    print(prediction)

