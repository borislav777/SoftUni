function timeToWalk(steps,meters,kmH) {
    let step = steps * meters;
    
    let speed = kmH / 3.6;
    let time = step/speed;
    let breaks = Math.trunc(step / 500);
    time += breaks*60;

    let hour =Math.trunc(time / 3600);
    let minute = Math.trunc(time % 3600/60);
    let seconds = Math.round(time % 60);
    console.log(`${hour.toString().padStart(2,0)}:${minute.toString().padStart(2,0)}:${seconds.toString().padStart(2,0)}`);
}   

timeToWalk(4000,0.60,5)