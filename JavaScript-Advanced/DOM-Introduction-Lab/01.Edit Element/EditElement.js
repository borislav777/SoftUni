function editElement(element, stringMatch,replacer) {
    let el = element.textContent;
    let pattern = new RegExp(stringMatch,'g');
   element.textContent = el.replace(pattern,replacer);
}