const buttonCarts = document.querySelectorAll(".add-cart");
    for (let buttonCart of buttonCarts) {
        buttonCart.onclick = function() {
            let requestAddCart = new XMLHttpRequest();
            let product = buttonCart.dataset;
            requestAddCart.open("GET", "/cart/" + product['id'] + "/add", true);
            requestAddCart.onload = function (){
                alert(product['name'] + ' in cart');
                buttonCart.textContent = 'in cart'
                buttonCart.setAttribute('disabled', '')
            }
            requestAddCart.send(null);
        }
    }