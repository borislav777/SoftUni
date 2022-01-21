function solve() {

    function fighter(name) {
        const fighter = {
            name,
            health: 100,
            stamina: 100,
            fight(){
                fighter.stamina --;
                console.log(`${fighter.name} slashes at the foe!`);
            }
        }
        return fighter;
    }
    function mage(name) {
        const mage = {
            name,
            health: 100,
            mana: 100,
            cast(spell){
                mage.mana --;
                console.log(`${mage.name} cast ${spell}`);
            }

        }
        return mage
    }
    return {fighter:fighter,mage:mage};

}

let create = solve();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball")
scorcher.cast("thunder")
scorcher.cast("light")

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight()

console.log(scorcher2.stamina);
console.log(scorcher.mana);