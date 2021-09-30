// Write a function that takes in a string of one or more words, and returns the same string, 
// but with all five or more letter words reversed.
// 
// - Strings passed in will consist of only letters and spaces.
// - Spaces will be included only when more than one word is present.
// 
// Examples:
// spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
// spinWords("This is a test") => "This is a test" 
// spinWords("This is another test") => "This is rehtona test"

function spinWords(string){
    sentenceArr = string.split(" ")
    
    for (let i = 0; i < sentenceArr.length; i++){
      if (sentenceArr[i].length > 4) {
        sentenceArr[i] = sentenceArr[i].split("").reverse().join("");
      }
    }
    
    return sentenceArr.join(" ").toString();
}