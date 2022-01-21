function wordsUppercase(text) {
    let pattern = /\w+/gm;
    let words = text.match(pattern)
    console.log(words.join(', ').toUpperCase());
}
wordsUppercase('Hi, how are')
wordsUppercase('you?')