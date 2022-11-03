const productItems = document.querySelector("#product-items");

function addProductToCart(btn) {
    let requestAddCart = new XMLHttpRequest();
    let product = btn.dataset;
    requestAddCart.open("GET", "/cart/" + product['id'] + "/add", true);
    requestAddCart.onload = function () {
        alert(product['name'] + ' in cart');
        btn.textContent = 'in cart'
        btn.setAttribute('disabled', '')
    };
    requestAddCart.send(null);
}

productItems.addEventListener('click', (event) => {
    let target = event.target;

    if (target.classList.contains('add-cart')) {
        addProductToCart(target);
    }
});