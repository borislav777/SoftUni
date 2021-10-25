class SummerCamp{
    constructor(organizer,location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = {"child": 150, "student": 300, "collegian": 500};
        this.listOfParticipants = [];
    }
    registerParticipant (name, condition, money){
        money = Number(money);
        if (this.priceForTheCamp.hasOwnProperty(condition)===false){
            throw Error("Unsuccessful registration at the camp.");
        }
        let findParti = this.listOfParticipants.filter((p)=>p.name === name)

        if (findParti.length>0){
            return `The ${name} is already registered at the camp.`
        }
        if(money < this.priceForTheCamp[condition]){
            return `The money is not enough to pay the stay at the camp.`
        }
        this.listOfParticipants.push({name,condition,power:100,wins:0})
        return `The ${name} was successfully registered.`
    }
    unregisterParticipant (name){
        let currParticipants = this.listOfParticipants.filter((p)=> p.name === name);
        if (currParticipants.length <= 0){
            throw Error(`The ${name} is not registered in the camp.`)
        }
        this.listOfParticipants.unshift(currParticipants[0])
        return `The ${name} removed successfully.`
    }
    timeToPlay (typeOfGame, participant1, participant2){
        let firstPlayer = this.listOfParticipants.filter((p)=> p.name === participant1);
        let secondPlayer = this.listOfParticipants.filter((p)=> p.name === participant2);
        if (typeOfGame === 'WaterBalloonFights') {


            if (firstPlayer.length <= 0 || secondPlayer.length <= 0) {
                throw Error(`Invalid entered name/s.`)
            }
            if (firstPlayer[0].condition !== secondPlayer[0].condition) {
                throw Error(`Choose players with equal condition.`)
            }
            if(firstPlayer[0].power > secondPlayer[0].power){
                firstPlayer[0].wins ++;
                return `The ${firstPlayer[0].name} is winner in the game ${typeOfGame}.`
            }else if(firstPlayer[0].power < secondPlayer[0].power){
                secondPlayer[0].wins ++;
                return `The ${secondPlayer[0].name} is winner in the game ${typeOfGame}.`
            }
            return `There is no winner.`;

        } else if (typeOfGame === 'Battleship'){
            if (firstPlayer.length <= 0) {
                throw Error(`Invalid entered name/s.`)
            }
            firstPlayer[0].power += 20;

            return `The ${firstPlayer[0].name} successfully completed the game ${typeOfGame}.`
        }
    }
    toString (){
        let result = [];
        result.push(`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`)
        let sortedParti = this.listOfParticipants.sort((a,b)=>b.wins - a.wins);
        for (const participant of sortedParti) {
            result.push(`${participant.name} - ${participant.condition} - ${participant.power} - ${participant.wins}`)
        }

        return result.join('\n');
    }

}



const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp.registerParticipant("Sara Dickinson", "child", 200));
// console.log(summerCamp.timeToPlay("WaterBalloonFights","Petar Petarson", "Sara Dickinson"));
console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));

console.log(summerCamp.toString());

