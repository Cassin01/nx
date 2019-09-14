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
        return [p[0], p[1].replace(' ', '')]
    })
    console.log('word.txtを読み込みました')

    const x = 1;
    switch (x) {
        case 1:
            task1(res)
            break
        case 2:
            task2(res)
            break
        case 3:
            task3(res)
            break
        default:
            task1(res)
            task2(res)
            task3(res)
    }
}

const task1 = (res) => {
    for (p of res) {
        console.log(p[0])


        scanf('%s')
        console.log(p[1])
        console.log()
        console.log()
    }
}

const task2 = (res) => {
    for (p of shuffle(res)) {
        console.log(p[0])


        scanf('%s')
        console.log(p[1])
        console.log()
        console.log()
    }
}

const task3 = (res) => {
    for (j in shuffle(res)) {
        const p = res[j]
        console.log(p[0])

        let d = [[parseInt(j), res[j][1]]]
        while (d.length != 3) {
            const index = parseInt(Math.random() * 10 % res.length)
            d.push([index, res[index][1]])
            d = dedup(d)
        }
        shuffle(d)
        console.log(d)

        const ans = scanf('%d')
        if (ans == j) {
            console.log('OK')
        } else {
            console.log('NO', p)
        }
        console.log('')
    }
}

const shuffle = (array) => {
  array.sort(() => Math.random() - 0.5)
  return array
}

const dedup = (arr) => {
	let hashTable = {}

	return arr.filter(function (el) {
		let key = JSON.stringify(el)
		let match = Boolean(hashTable[key])

		return (match ? false : hashTable[key] = true)
	})
}

const scanf = require('scanf')

const main = () => {
    read()
}

main()
