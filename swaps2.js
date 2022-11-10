function minimumSwaps(arr) {
    let i = 0;
    let count = 0;
    while (i < arr.length) {
        let num = arr[i]
        if (arr[i] !== i + 1) {
            const newValue = arr[num - 1];
            arr[num - 1] = num;
            arr[i] = newValue;
            count++;
        } else {
            i++;
        }
    }
    return count;
}
