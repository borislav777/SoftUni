function townToJSON(arr) {
    const towns = [];
    for (let i = 1; i < arr.length; i++) {
        let [town,latitude,longitude] = arr[i].slice(2,-2).split(' | ');
        latitude = Number(Number(latitude).toFixed(2));
        longitude = Number(Number(longitude).toFixed(2));
        towns.push({
            Town:town,
            Latitude: latitude,
            Longitude: longitude
        });

        
    }
    console.log(JSON.stringify(towns));
}
townToJSON(
    ['| Town | Latitude | Longitude |',
'| Sofia | 42.696552 | 23.32601 |',
'| Beijing | 39.913818 | 116.363625 |']
);