function attachEvents() {
    let div = document.getElementById('forecast');
    let errDiv = document.createElement('div')
    const locationField = document.getElementById('location');
    errDiv.textContent = 'Error';
    div.appendChild(errDiv)
    const button = document.getElementById('submit');
    button.addEventListener('click', getWeather);
    let divCurrConditions = document.getElementById('current');
    const divUpcomingConditions = document.getElementById('upcoming');
    const weatherSymbols = {
        'Sunny': '&#x2600',
        'Partly sunny': '&#x26C5',
        'Overcast': '&#x2601',
        'Rain': '&#x2614;',
        'Degrees': '&#176'
    }
    async function getWeather() {
        div.style.display = 'none';
        errDiv.style.display = 'none';
        divUpcomingConditions.style.display= 'block';
        divCurrConditions.style.display = 'block'
        clear(divCurrConditions);
        clear(divUpcomingConditions);
        let code;

        try {
            code = await getCode(locationField.value);
            if (!code) {
                throw new Error('Error');
            }
            let  [current, threeDays] = await Promise.all([
                getCurrentConditions(code),
                getThreeDaysConditions(code)
            ]);
            locationField.value = '';
            const divForecast = document.createElement('div');
            divForecast.className = 'forecast';
            divForecast.appendChild(newElement('span', {
                className: 'condition symbol',
                innerHTML: weatherSymbols[current.forecast.condition]
            }))
            const condition = document.createElement('span');
            condition.className = 'condition';
            condition.appendChild(newElement('span', {className: 'forecast-data'}, current.name))
            condition.appendChild(newElement('span', {
                className: 'forecast-data',
                innerHTML: `${current.forecast.low}&#176;/${current.forecast.high}&#176;`
            }))
            condition.appendChild(newElement('span', {className: 'forecast-data'}, current.forecast.condition))
            divForecast.appendChild(condition);
            divCurrConditions.appendChild(divForecast);

            const divForecastInfo = document.createElement('div');
            divForecastInfo.className = 'forecast-info';

            for (const day of threeDays.forecast) {
                const conditionUpcoming = document.createElement('span');
                conditionUpcoming.className = 'upcoming';
                conditionUpcoming.appendChild(newElement('span', {
                    className: 'symbol',
                    innerHTML: weatherSymbols[day.condition]
                }))
                conditionUpcoming.appendChild(newElement('span', {
                    className: 'forecast-data',
                    innerHTML: `${day.low}&#176;/${day.high}&#176;`
                }))
                conditionUpcoming.appendChild(newElement('span', {className: 'forecast-data'}, day.condition))
                divForecastInfo.appendChild(conditionUpcoming);
            }
            divUpcomingConditions.appendChild(divForecastInfo);
            div.style.display = 'block';

        } catch (error) {
            div.style.display = 'block';
            document.getElementById('current').style.display = 'none';
            document.getElementById('upcoming').style.display = 'none';
            errDiv.style.display = 'block';

        }

    }

}

attachEvents();
async function getCode(name) {
    const url = 'http://localhost:3030/jsonstore/forecaster/locations';
    const result = await fetch(url);
    const data = await result.json();
    const code = Object.values(data).find(el => el.name === name);
    return code.code;
}

async function getCurrentConditions(code) {
    const url = 'http://localhost:3030/jsonstore/forecaster/today/' + code;
    const result = await fetch(url);
    const data = await result.json();
    return data;
}

async function getThreeDaysConditions(code) {
    const url = 'http://localhost:3030/jsonstore/forecaster/upcoming/' + code;
    const result = await fetch(url);
    const data = await result.json();
    return data;
}

function clear(div) {
    while (div && div.children.length > 1) {
        div.removeChild(div.lastChild);
    }
}

function newElement(type, props, ...content) {
    const element = document.createElement(type);
    for (let prop in props) {
        element[prop] = props[prop];
    }
    for (let entry of content) {
        if (typeof entry == 'string' || typeof entry == 'number') {
            entry = document.createTextNode(entry);
        }
        element.appendChild(entry);
    }

    return element;
}







