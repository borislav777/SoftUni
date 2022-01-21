function arrSort(arr) {
    arr.sort((a, b) => {
        if (a.length > b.length) {
            return 1;
        } else if (a.length == b.length) {
            return a.localeCompare(b);
        } else {
            return - 1;
        }
    })
    console.log(arr.join('\n'));
}
arrSort(
    ['alpha',
        'beta',
        'gamma']
)