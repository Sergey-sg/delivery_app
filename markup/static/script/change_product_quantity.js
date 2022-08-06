const productItems = document.querySelector('#product-items');

function addProductToCart(btn) {
    let requestAddCart = new XMLHttpRequest();
    let product = btn.dataset;
    requestAddCart.open("GET", "/cart/" + product['id'] + "/add", true);
    requestAddCart.send(null);
}

productItems.addEventListener('click', (event) => {
    let target = event.target.parentNode;

    if (target.classList.contains('add-cart')) {
        event.preventDefault()
        addProductToCart(target);
    }
});