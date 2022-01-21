function playingCards(face,suit) {
    const faces = ['2', '3', '4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
    if (!faces.includes(face)){
        throw new Error('Error')
    }
    const suits = {
        S: '\u2660',
        H: '\u2665',
        D: '\u2666',
        C: '\u2663'
    }
    return {
        face,
        suit:suits[suit],
        toString(){
            return this.face + this.suit
    }
    }
}

console.log(playingCards('A', 'S').toString())
console.log(playingCards('10', 'H').toString())
console.log(playingCards('1', 'S').toString())