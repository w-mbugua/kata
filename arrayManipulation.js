/*
problem:
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, 
inclusive. Once all operations have been performed, return the maximum value in the array.
*/

function arrayManipulation(n, queries) {
    let arr = Array(n).fill(0);

    for (let query of queries) {
        const k = query[2];
        for (let a = query[0]; a <= query[1]; a++) {
            if (a <= arr.length) {
                arr[a - 1] = arr[a - 1] + k;
            }
        }
    }
    return Math.max(...arr)
}
