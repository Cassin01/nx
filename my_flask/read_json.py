import json


def read():
    with open("data/myu_s.json", 'r') as f:
        jsn = json.load(f)

    data = []
    for key in jsn:
        en = jsn[key]["japanese"]
        data.append([key, en])
    return data
