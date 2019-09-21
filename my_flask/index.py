from flask import Flask, render_template

import random
import read_json
import retrive

app = Flask(__name__)
#    FLASK_APP="index.py" FLASK_ENV=development flask run


try:
    data = read_json.read()
except Exception as e:
    print(f"例外検知: {str(e)}")


class Word:
    eng = ""
    times = 0
    ok_times = 0

    def __init__(self, eng):
        self.eng = eng
        self.times = 0
        self.ok_times = 0


def srch(eng, ls):
    for i, l in enumerate(ls):
        if l.eng == eng:
            return i
    return -1


target =[]
for d in data:
    word = Word(d[0])
    target.append(word)

# メニューを表示
@app.route("/")
def menu():
    num = random.randrange(0, len(data))
    english = data[num][0]
    japanese = data[num][1]

    ts = [[data[num][1], "ok"]]
    while len(ts) < 4:
        row = data[random.randrange(0, len(data))][1]
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
