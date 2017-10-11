import math


def is_const(data, dim, numData, mu):
    sigma = []
    _numData = math.ceil(len(data) / dim)
    for i in range(0, _numData * dim):
        sigma[i % dim] = sigma[i % dim] or 0
        datum = data[i] or mu
        sigma[i % dim] += (datum - mu) * (datum - mu) / numData

    sigma = [math.sqrt(_sigma) for _sigma in sigma]
    return {"mu": [mu], "sigma": sigma}
