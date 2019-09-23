import json


class Word:
    eng = ""
    jp = ""
    times = 0
    ok_times = 0

    def __init__(self, eng, jp, times, ok_times):
        self.eng = eng
        self.jp = jp
        self.times = times
        self.ok_times = ok_times


def read():
    with open("data/myu_s.json", 'r') as f:
        jsn = json.load(f)

    data = []
    for key in jsn:
        jp = jsn[key]["japanese"]
        try_times = jsn[key]["times"]
        ok_times = jsn[key]["ok_times"]
        w = Word(key, jp, try_times, ok_times)
        data.append(w)
    return data
