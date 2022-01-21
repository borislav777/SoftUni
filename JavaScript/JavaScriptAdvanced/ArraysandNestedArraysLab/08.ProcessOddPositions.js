function processOddPositions(arr) {
    let result = arr.filter((v, i) => i % 2 == 1)
        .map((a) => a * 2)
        .reverse()
    console.log(...result);
}
processOddPositions([10, 15, 20, 25]
)
processOddPositions([3, 0, 10, 4, 7, 3]

)