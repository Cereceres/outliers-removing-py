def complete_data(data, numData, dim):
    total_data = numData * dim
    if total_data > len(data):
        data = data + data[0: total_data - len(data)]
    if total_data > len(data):
        return complete_data(data, numData, dim)
    return data
