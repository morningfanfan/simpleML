def check_data_format(data):

    if len(data) == 4 and all(type(i) == int for i in data):
        return True
    else:
        raise IndexError


def check_idx_format(idx):
    return int(idx)
