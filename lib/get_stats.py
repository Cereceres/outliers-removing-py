from is_const import is_const
from is_func import is_func
import math


def get_stats(data, dim=1, dg=0, timeSeries=None):
    numData = math.ceil(len(data) / dim)
    mu = timeSeries or []

    if type(mu) is int or type(mu) is float:
        return is_const(data, dim, numData - dg, mu)

    if callable(mu):
        return is_func(data, dim, numData - dg, mu)

    sigma = []
    print 'mu ', mu
    for i in range(int(numData * dim)):
        mu[i % dim] = mu[i % dim]
        datum = data[i] or mu[i % dim]
        mu[i % dim] += datum / numData
    for i in range(numData * dim):
        sigma[i % dim] = sigma[i % dim] or 0
        if not data.get(i):
            continue
        pivot = (data[i] - mu[i % dim]) * (data[i] - mu[i % dim])
        pivot /= numData - dg
        sigma[i % dim] += pivot

    sigma = [math.sqrt(_sigma) for _sigma in sigma]
    return {"mu": mu, "sigma": sigma}
