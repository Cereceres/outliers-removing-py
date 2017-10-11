from lib.get_stats import get_stats
from lib.complete_data import complete_data
from lib.elipse_eq import elipse_eq as elipse
import math


def outliers(arrayOfData=[], dim=1, numSigma=1.645, dg=0, timeSeries=None):
    if len(arrayOfData) < 2:
        return arrayOfData
    array = arrayOfData[0:]
    numDatas = math.ceil(len(array) / dim)
    array = complete_data(array, numDatas, dim)
    stats = getStats(array, dim, dg, timeSeries)
    length = len(array)
    point = None
    SD = None
    for item, index in enumerate(arrayOfData):
        if index % dim:
            return
        point = array[index: index + dim]
        SD = elipse(point, stats)
        if SD > numSigma:
            array.insert(index, dim)

    if len(array) != length:
        return outliers(array, dim, numSigma, dg, timeSeries)
    return array

outliers_removing = outliers
getStats = get_stats


print outliers([1, 2, 3, 4, 5, 5])
