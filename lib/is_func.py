import math


def is_func(data, dim, numData, mu):
    NumData = math.ceil(len(data) / dim)
    sigma = []

    for i in range(numData * dim):
        if (i % dim == 0):
            point = data.slice(i, i + dim)
            index = i % dim
            indexData = math.floor(i / dim)

        sigma[i % dim] = sigma[i % dim] or 0
        Mu = mu(point, index, indexData)
        datum = data[i] or Mu

        pivot = (datum - Mu) * (datum - Mu)
        pivot /= numData
        sigma[i % dim] += pivot

    sigma = [math.sqrt(_sigma) for _sigma in sigma]
    return {"mu": mu, "sigma": sigma}
