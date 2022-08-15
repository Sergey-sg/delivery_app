const productItems = document.querySelector('#cart-items');

async function addToCartItem(url) {
    try {
        let response = await fetch(url, {method: "GET"});
        if (response.status === 200) {
            return await response;
        }
    } catch (error) {
        console.log(error);
    }
}

async function addProductToCart(btn) {
    let product = btn.dataset;
    let cartItemSubTotal = btn.parentNode.previousElementSibling;
    let cartItemQuantity = cartItemSubTotal.previousElementSibling.querySelector('#quantity')
    let cartTotalPrice = document.body.querySelector('#total-price')
    let url = "/cart/" + product['id'] + "/add";
    let cartItem = await addToCartItem(url)
        .then((response) => response.json())
        .then((data) => data);
    cartItemSubTotal.textContent = '$' + cartItem['sub_total'];
    cartItemQuantity.textContent = 'Quantity: ' + cartItem['quantity'] + ' x ' + cartItem['product_name'];
    cartTotalPrice.textContent = cartItem['total'];
}

productItems.addEventListener('click', (event) => {
    let target = event.target.parentNode;

    if (target.classList.contains('add-cart')) {
        event.preventDefault();
        addProductToCart(target);
    }
});