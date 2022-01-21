function attachEventsListeners() {
    const rations = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    }
    function converter(value,inputUnits,outputUnits){
        return value * rations[inputUnits] / rations[outputUnits];

    }
    document.getElementById('convert').addEventListener('click',onClick);

    function onClick(evt){
        let input = Number(document.getElementById('inputDistance').value);
        let inUnit = document.getElementById('inputUnits').value;
        let outUnit = document.getElementById('outputUnits').value;
        let output = document.getElementById('outputDistance');
        output.value = converter(input,inUnit,outUnit)

    }

}