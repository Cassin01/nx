const fs = require('fs')

// 非同期でファイルを読み込みPromiseを返す関数を定義
const readFileEx = (filePath) => {
    return new Promise((resolve, reject) => {
        fs.readFile(path = filePath, options = {
            encoding: 'utf8'
        }, (err, data) => {
            resolve(data)
        })
    })
}


// すべてのファイルを非同期に読み込むasync関数を定義
const read = async() => {
    const text = await readFileEx('word.txt')
    const res = text.split('\n').filter(l => l != '').map((p) => {
        p = p.split(':');
        if (p[1].slice(0, 1) == ' ') {
            return [p[0], p[1].slice(1)]
        } else {
            return p
        }
    })
    console.log('word.txtを読み込みました')

    runer(res)
}

const runer = (res) => {
    while (true) {
        p = res.shift();
        console.log(p[0])

        scanf('%s')

        console.log(p[1])
        console.log()
        let ans = scanf('%s')
        
        switch (ans) {
            case "q":
                return;
            case "s":
                res.splice(parseInt(res.length / 2), 0, p)
                break;
            case "d":
                res.splice(parseInt(res.length / 2 / 2), 0, p)
                break;
            default:
                res.push(p)
                break;
        }
    }
}

const scanf = require('scanf')

const main = () => {
    read()
}

main()
