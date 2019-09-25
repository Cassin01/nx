
from flask import Flask, render_template

import random
import read_json
import retrive
import update_json

update_json.update()

app = Flask(__name__)
#    FLASK_APP="index.py" FLASK_ENV=development flask run


try:
    data = read_json.read()
except Exception as e:
    print(f"例外検知: {str(e)}")


class Word:
    def __init__(self, eng, jp, times, ok_times):
        self.jp = jp
        self.eng = eng
        self.times = times
        self.ok_times = ok_times


def srch(eng, ls):
    for i, l in enumerate(ls):
        if l.eng == eng:
            return i
    return -1


target = []
for d in data:
    word = Word(d[0], d[1], d[2], d[3])
    target.append(word)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/show")
def show():
    ds = []
    for t in target:
        rate = 0. if t.times == 0 else t.ok_times / t.times
        ds.append([t.eng, t.jp, rate])

    ds = sorted(ds, key=lambda t: t[2])

    return render_template("show.html", ds=ds)


# メニューを表示
@app.route("/easy")
def menu():
    num = random.randrange(0, len(target))
    english = target[num].eng
    japanese = target[num].jp

    ts = [[target[num].jp, "ok"]]
    while len(ts) < 4:
        row = target[random.randrange(0, len(target))].jp
        if [row, "no"] not in ts and [row, "ok"] not in ts:
            ts.append([row, "no"])
    random.shuffle(ts)
    return render_template("index.html", english=english, japanese=japanese, ts=ts)


@app.route("/hard")
def menu_hard():
    num = random.randrange(0, len(target))
    english = target[num].eng
    japanese = target[num].jp

    ts = [[target[num].jp, "ok"]]
    while len(ts) < 4:
        row = target[random.randrange(0, len(target))].jp
        if [row, "no"] not in ts and [row, "ok"] not in ts:
            ts.append([row, "no"])
    random.shuffle(ts)
    return render_template("index.html", english=english, japanese=japanese, ts=ts)

# OK
@app.route("/ok/<info>")
def fok(info=None):
    eng = retrive.retrive(info)
    eng = srch(eng, target)
    target[eng].times += 1
    target[eng].ok_times += 1
    menu_name = "OK"
    return render_template("screen_tran.html", menu_name=menu_name,
            info=info, times=target[eng].times, ok_times=target[eng].ok_times)

# NO
@app.route("/no/<info>")
def fno(info=None):
    eng = retrive.retrive(info)
    eng = srch(eng, target)
    target[eng].times += 1
    menu_name = "NO"
    return render_template("screen_tran.html", menu_name=menu_name,
            info=info, times=target[eng].times, ok_times=target[eng].ok_times)


@app.route("/save")
def save():
    import json
    import collections as cl
    ys = cl.OrderedDict()

    for t in target:
        tmp_data = cl.OrderedDict()
        tmp_data["japanese"] = t.jp
        tmp_data["times"] = t.times
        tmp_data["ok_times"] = t.ok_times
        ys[t.eng] = tmp_data

    try:
        fw = open('data/myu_s.json', 'w')
        json.dump(ys, fw, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)
    finally:
        fw.close()
    return render_template("save.html")
