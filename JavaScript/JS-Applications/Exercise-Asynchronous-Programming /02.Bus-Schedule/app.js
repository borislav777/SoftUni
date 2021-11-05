function solve() {
    const spanInfo = document.querySelector('#info span');
    const arriveBtn = document.getElementById('arrive');
    const departBtn = document.getElementById('depart');
    let nextStopId = 'depot';
    let nextStopName = 'Depot';


    async function depart() {
        departBtn.disabled = true;
        const url = `http://localhost:3030/jsonstore/bus/schedule/${nextStopId}`;
        try {
            const result = await fetch(url);
            if (result.status !== 200) {
                throw new Error('Error');
            }
            const data = await result.json();
            spanInfo.textContent = `Next stop ${data.name}`
            nextStopId = data.next;
            nextStopName = data.name;
            arriveBtn.disabled = false;

        } catch (error) {
            spanInfo.textContent = error.message;
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        }


    }

    function arrive() {

        spanInfo.textContent = `Arriving at ${nextStopName}`
        departBtn.disabled = false;
        arriveBtn.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();