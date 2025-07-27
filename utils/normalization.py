from get_data import get_list


def normalize(list, data):
    return ((data - min(list)) / (max(list) - min(list)))


def data_normalization(data, arg):
    list = get_list(data, arg)
    normalize_list = []

    for d in list:
        n = normalize(list, d)
        normalize_list.append(n)

    return normalize_list