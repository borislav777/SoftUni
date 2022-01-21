function generateReport() {
    const report = [];
    let employees = document.querySelectorAll('tbody tr');
    let header = document.querySelectorAll('thead tr th');
    
    for (const employee of employees) {
        let result = {}
        for (let i = 0; i < header.length; i++) {
        
            if (header[i].lastElementChild.checked){
                result[header[i].lastElementChild.name] = employee.cells[i].textContent;
                
            }
            
        }
        report.push(result);
    
        
    }
    document.getElementById('output').value =JSON.stringify(report);
    
    
}