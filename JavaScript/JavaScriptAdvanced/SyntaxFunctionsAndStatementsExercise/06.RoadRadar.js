function roadRadar(speed, area) {
    speed = Number(speed);
    let speedLimit;
    switch (area) {
        case 'motorway':
            speedLimit = 130;
            break;
        case 'interstate':
            speedLimit = 90;
            break;
        case 'city':
            speedLimit = 50;
            break;
        case 'residential':
            speedLimit = 20;
            break;

    }
    let difference = speed - speedLimit;
    let speedStatus;

    if (speed <= speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    } else {
        if (difference <= 20) {
            speedStatus = 'speeding';
        }
        else if (difference <= 40) {
            speedStatus = 'excessive speeding';
        } else {
            speedStatus = 'reckless driving';
        }
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${speedStatus}`);
    }
}
roadRadar(40, 'city')
roadRadar(21, 'residential')
roadRadar(120, 'interstate')
roadRadar(200, 'motorway')
