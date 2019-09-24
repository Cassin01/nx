import json


def read():
    with open("data/myu_s.json", 'r') as f:
        jsn = json.load(f)

    data = []
    for key in jsn:
        en = jsn[key]["japanese"]
        times = jsn[key]["times"]
        ok_times = jsn[key]["ok_times"]
        data.append([key, en, times, ok_times])
    return data
