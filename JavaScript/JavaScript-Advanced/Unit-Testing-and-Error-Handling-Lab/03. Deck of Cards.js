function deckOfCards(arr) {
    let result = [];
    for (const card of arr) {
        let face = card.slice(0, -1);
        let suit = card.slice(-1);
        try {
            result.push(playingCards(face,suit));
        }catch (err){
            console.log(`Invalid card: ${card}`);
            return;
        }

    }
    console.log(result.join(' '));


    function playingCards(face, suit) {
        const faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
        if (!faces.includes(face)) {
            throw new Error('Error')
        }


        const suits = {
            S: '\u2660',
            H: '\u2665',
            D: '\u2666',
            C: '\u2663'
        }
        if (!Object.keys(suits).includes(suit)) {
            throw new Error('Error')
        }
        return {
            face,
            suit: suits[suit],
            toString() {
                return this.face + this.suit
            }
        }
    }
}

deckOfCards(['5S', '3D', 'QD', '1C'])
deckOfCards(['AS', '10D', 'KH', '2C'])