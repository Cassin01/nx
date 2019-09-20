def edit(text):
    text = text.split('\n')
    text = list(filter(lambda x: x != '', text))
    text = list(map(lambda x: x.split(':'), text))
    text = list(map(lambda x: [x[0], x[1][1:]] if x[1][0] == ' ' else x, text))
    return text

# 読込むファイルのパスを宣言する
file_name = "./word.txt"

def read():
    try:
        file = open(file_name)
        data = file.read()
    except Exception as e:
        print(e)
    finally:
        file.close()

    return edit(data)
