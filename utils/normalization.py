from utils.get_data import get_list


def normalize(list: list[str], data: str):
    return ((data - min(list)) / (max(list) - min(list)))


def data_normalization(data: list[str], arg: str):
    list = get_list(data, arg)
    normalized_list = []

    for d in list:
        n = normalize(list, d)
        normalized_list.append(n)

    return normalized_list