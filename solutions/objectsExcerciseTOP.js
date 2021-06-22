// Exercise:

// Write a constructor for making “Book” objects. We will revisit this in the project at the end of this lesson. Your book objects should have the book’s title, author, the number of pages, and whether or not you have read the book

// Put a function into the constructor that can report the book info like so: theHobbit.info() 
// "The Hobbit by J.R.R. Tolkien, 295 pages, not read yet"

// note: it is almost always best to return things rather than putting console.log() directly into the function. In this case, return the info string and log it after the function has been called:  console.log(theHobbit.info());


function Book(title, author, numberOfPages, haveRead){
    this.title = title;
    this.author = author;
    this.numberOfPages = numberOfPages;
    this.haveRead = haveRead;

    this.info = function() {
        return title + " by " + author + ", " + numberOfPages + " pages, " + haveRead;
    }
}

const theHobbit = new Book('The Hobbit', 'J.R.R. Tolkien', '295', 'not read yet')
console.log(theHobbit.info());



// Use __proto__ to assign prototypes in a way that any property lookup will follow the path: pockets → bed → table → head. 
// For instance, pockets.pen should be 3 (found in table), and bed.glasses should be 1 (found in head).
// Answer the question: is it faster to get glasses as pockets.glasses or head.glasses? Benchmark if needed.


let head = {
    glasses: 1
  };
  
  let table = {
    pen: 3,
    __proto__: head
  };
  
  let bed = {
    sheet: 1,
    pillow: 2,
    __proto__: table
  };
  
  let pockets = {
    money: 2000,
    __proto__: bed
  };

  console.log(pockets.pen)
  console.log(bed.glasses)