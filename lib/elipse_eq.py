import math


def elipse_eq(point, stats):
    def reducer(init, coord, index):
        if not stats.sigma[index % len(stats.sigma)]:
            return init
        if callable(stats.mu):
            mu = stats.mu(point, index)
        else:
            mu = stats.mu[index % len(stats.mu)]
        SD = (coord - mu) * (coord - mu)
        SD /= stats.sigma[index % len(stats.sigma)] * stats.sigma[
            index % len(stats.sigma)]
        return init + SD
    sd = reduce(reducer, point, 0)
    return math.sqrt(sd)
