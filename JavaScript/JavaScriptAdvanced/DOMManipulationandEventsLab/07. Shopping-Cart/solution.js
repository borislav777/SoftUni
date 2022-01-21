function solve() {
    document.getElementsByClassName('shopping-cart')[0].addEventListener('click',onClick);
    let output = document.getElementsByTagName('textarea')[0];
    document.getElementsByClassName('checkout')[0].addEventListener('click',checkout);
    const cart = [];
    function onClick(evt){
        if (evt.target.tagName === 'BUTTON' && evt.target.classList.contains('add-product')){
            const product = evt.target.parentNode.parentNode;
            const name = product.querySelector('.product-title').textContent;
            const price = Number(product.querySelector('.product-line-price').textContent);

            cart.push({
                name,
                price
            });
            output.textContent += `Added ${name} for ${price.toFixed(2)} to the cart.\n`
        }
    }
    function checkout(){
        const products = new Set();
        cart.forEach((p)=>products.add(p.name));
        const sumAll = cart.reduce((t,c)=>t + c.price,0)
        output.textContent += `You bought ${Array.from(products.keys()).join(', ')} for ${sumAll.toFixed(2)}.`
        document.getElementsByClassName('checkout')[0].removeEventListener('click',checkout);
        document.getElementsByClassName('shopping-cart')[0].removeEventListener('click',onClick);

    }


}