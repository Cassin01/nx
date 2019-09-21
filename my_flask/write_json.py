import json
import collections as cl

import read

def main():
    name_list = read.read()
    ys = cl.OrderedDict()
    for d in name_list:
        data = cl.OrderedDict()
        data["japanese"] = d[1]
        data["times"] = 0
        data["ok_times"] = 0

        ys[d[0]] = data
    print("{}".format(json.dumps(ys, indent=4)))

    try:
        fw = open('data/myu_s.json', 'w')
        json.dump(ys, fw, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)
    finally:
        fw.close()


if __name__ == '__main__':
    main()
