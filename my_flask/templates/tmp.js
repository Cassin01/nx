const retriveEnglish = (word) => {
		let str = ""
		let arr = genAlphabetArray()
		for (let c of word) {
				if (arr.indexOf(c) >= 0 || c == ' ') { // 存在する
						str += c
				} else {
						break
				}
		}
		return str
}
const genAlphabetArray = () => {
		var a = [], i = 'a'.charCodeAt(0), j = 'z'.charCodeAt(0);
		for (; i <= j; ++i) {
				a.push(String.fromCharCode(i));
		}
		return a;
}

console.log(retriveEnglish("fla jflfjうんこ大好き "))
