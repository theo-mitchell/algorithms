/**
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character, but a character may map to itself.
**/

function isIsomorphic(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    
    let hashMap: any = {};
    let isomorphic: boolean = true;

    for (let i = 0; i < s.length; i++) {
        if (!hashMap[s[i]]) {
            hashMap[s[i]] = t[i];
        } else if ((hashMap[s[i]] && hashMap[s[i]] !== t[i])) {
            isomorphic = false;
            break;
        }
    };

    if (new Set(Object.values(hashMap)).size !== Object.values(hashMap).length) return false;

    return isomorphic;
}