function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
      let data = JSON.parse(document.querySelector('textarea').value);
      let restaurants = {};

      for (const restaurant of data) {
         let [restaurantName, workersString] = restaurant.split(' - ');
         inputWorkers = workersString.split(', ').map((el) => {
            let [name, salary] = el.split(' ')
            return { name, salary: Number(salary) };
         })
         if (!restaurants[restaurantName]) {
            restaurants[restaurantName] = {
               restaurantName,
               workers: [],
               getAverage() {
                  return this.workers.reduce((acc, s) => acc + s.salary, 0) / this.workers.length;
               }
            }
         }
         restaurants[restaurantName].workers = restaurants[restaurantName].workers.concat(inputWorkers);

      }
      let sorttedRestaurants = Object.values(restaurants).sort((a, b) => b.getAverage() - a.getAverage());
      let sorttedWorkers = Object.values(sorttedRestaurants[0].workers).sort((a, b) => b.salary - a.salary);
      document.querySelector('#bestRestaurant p').textContent = `Name: ${sorttedRestaurants[0].restaurantName} Average Salary: ${sorttedRestaurants[0].getAverage().toFixed(2)} Best Salary: ${sorttedWorkers[0].salary.toFixed(2)}`
      document.querySelector('#workers p').textContent = sorttedWorkers.map((w) => `Name: ${w.name} With Salary: ${w.salary}`).join(' ')
   }
}