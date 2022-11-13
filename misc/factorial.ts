function factorial(n: number): number {
    if (n === 0 || n === 1) {
        return 1
    } else {
        return n * (factorial(n - 1));
    }
}

console.log(factorial(10));
console.log(10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1);
