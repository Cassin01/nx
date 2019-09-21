def retrive(text: str) -> str:
    res = ""
    for c in text:
        if c == ':':
            return res
        else:
            res += c
