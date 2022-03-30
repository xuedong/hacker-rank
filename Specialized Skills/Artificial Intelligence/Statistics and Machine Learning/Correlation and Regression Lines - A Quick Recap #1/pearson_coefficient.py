#!/usr/bin/env python3

import numpy as np


if __name__ == "__main__":
    physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
    history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

    n = len(physics)
    mp = np.mean(physics)
    mh = np.mean(history)

    numerator = np.sum([(physics[i]-mp)*(history[i]-mh) for i in range(n)])
    sigmap = np.sqrt(np.sum([(physics[i]-mp)**2 for i in range(n)]))
    sigmah = np.sqrt(np.sum([(history[i]-mh)**2 for i in range(n)]))

    rho = numerator / (sigmap * sigmah)
    print(round(rho, 3))

