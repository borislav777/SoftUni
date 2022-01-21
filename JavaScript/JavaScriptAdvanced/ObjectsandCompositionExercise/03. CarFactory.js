function carFactory(car) {
    
    const configCar = {
        model: car.model,
        engine: carEngine(car),
        carriage : {
            type: car.carriage,
            color: car.color
        },
        wheels: carWheels(car.wheelsize)
    }
    function carWheels(size) {
        let wheels = new Array(4);
        
        if (size % 2 == 0) {
            size --;
        }
        wheels.fill(size);
        return wheels;
    }
    function carEngine(obj) {
        let engine;
        if (obj.power <= 90){
            engine = {
                power:90,
                volume: 1800
            }
        }else if (obj.power <= 120){
            engine = {
                power:120,
                volume: 2400
            }
        }else{
            engine = {
                power:200,
                volume: 3500
            }
        }
        return engine;
    }
    return configCar;
}
console.log(carFactory(
    { model: 'Opel Vectra',
    power: 110,
    color: 'grey',
    carriage: 'coupe',
    wheelsize: 17 }
));