from flask import Flask, render_template

import random
import read_json

app = Flask(__name__)
#    FLASK_APP="index.py" FLASK_ENV=development flask run


try:
    data = read_json.read()
except Exception as e:
    print(f"例外検知: {str(e)}")


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
    menu_name = "OK"
    return render_template("screen_tran.html", menu_name=menu_name, info=info)

# NO
@app.route("/no/<info>")
def fno(info=None):
    menu_name = "NO"
    return render_template("screen_tran.html", menu_name=menu_name, info=info)
