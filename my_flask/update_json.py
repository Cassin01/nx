import read
import read_all_json_data


def gain_update_data():
    text_data = read.read()
    json_data = read_all_json_data.read()

    eng_data = []
    for json_d in json_data:
        eng_data.append(json_d.eng)

    new_data = []
    for text_d in text_data:
        if text_d[0] not in eng_data:
            new_data.append(text_d)

    # update Json data
    for new_d in new_data:
        w = read_all_json_data.Word(new_d[0], new_d[1], 0, 0)
        json_data.append(w)

    return json_data


def write_json(ws):
    import json
    import collections as cl
    ys = cl.OrderedDict()
    for d in ws:
        data = cl.OrderedDict()
        data["japanese"] = d.jp
        data["times"] = d.times
        data["ok_times"] = d.ok_times

        ys[d.eng] = data
    print("{}".format(json.dumps(ys, indent=4)))

    try:
        fw = open('data/myu_s.json', 'w')
        json.dump(ys, fw, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)
    finally:
        fw.close()


def main():
    ds = gain_update_data()
    write_json(ds)


if __name__ == "__main__":
    main()
