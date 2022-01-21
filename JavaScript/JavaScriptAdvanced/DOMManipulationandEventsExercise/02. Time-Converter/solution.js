function attachEventsListeners() {
    const ratios = {
        days : 1,
        hours: 24,
        minutes : 1440,
        seconds : 86400
    }
    function convert(value,unit){
        const inDays = value / ratios[unit];
        return {
            days : inDays,
            hours : inDays * ratios.hours,
            minutes : inDays * ratios.minutes,
            seconds : inDays * ratios.seconds

        }
    }
    document.querySelector('main').addEventListener('click',onClick);

    function onClick(evt){
        if (evt.target.tagName === 'INPUT' && evt.target.type === 'button'){
            const input = evt.target.parentElement.querySelector('input[type = "text"]');
            const time = convert(Number(input.value),input.id)
            document.getElementById('days').value = time.days;
            document.getElementById('hours').value = time.hours;
            document.getElementById('minutes').value = time.minutes;
            document.getElementById('seconds').value = time.seconds;
        }
    }



}