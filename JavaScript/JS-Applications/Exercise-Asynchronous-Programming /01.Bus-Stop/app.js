async function getInfo() {
    const stopNumber = document.getElementById('stopId').value;
    const divStopName = document.getElementById('stopName');
    const ulBuses = document.getElementById('buses');
    const url = `http://localhost:3030/jsonstore/bus/businfo/${stopNumber}`


    try {
        divStopName.textContent= 'Loading...';
        ulBuses.replaceChildren();
        const result = await fetch(url);
        if (result.status !== 200) {
            throw new Error('Error');
        }
        const data = await result.json();

        divStopName.textContent = data.name;
        for (const [bus, time] of Object.entries(data.buses)) {
            const li = document.createElement('li');
            li.textContent = `Bus ${bus} arrives in ${time} minutes`
            ulBuses.appendChild(li);
        }
    } catch (error) {
        divStopName.textContent = error.message;
    }


}