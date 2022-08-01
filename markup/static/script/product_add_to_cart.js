const buttonCarts = document.querySelectorAll(".add-cart");

function addProductToCart() {
    let requestAddCart = new XMLHttpRequest();
    let product = this.dataset;
    let btn = this;
    requestAddCart.open("GET", "/cart/" + product['id'] + "/add", true);
    requestAddCart.onload = function () {
        alert(product['name'] + ' in cart');
        btn.textContent = 'in cart'
        btn.setAttribute('disabled', '')
    }
    requestAddCart.send(null);
}

for (let buttonCart of buttonCarts) {
    buttonCart.addEventListener('click', addProductToCart);
}