function isSubsequence(s: string, t: string): boolean {
    let sArray = s.split('');
    let tArray = t.split('');
    let searchedLetter = sArray.shift();

    if (tArray.length === 1) {
        return tArray[0] === searchedLetter;
    }

    for (let letter of tArray) {
        if (letter === searchedLetter) {
            searchedLetter = sArray.shift();
            if (sArray.length === 0) {
                continue;
            }
        }
    }

    return sArray.length === 0 && searchedLetter == null;
};