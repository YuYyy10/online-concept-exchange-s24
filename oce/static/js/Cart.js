function addToCart(product) {
    let cart = JSON.parse(localStorage.getItem("cart")) || []; // Retrieve existing cart or initialize empty array
    cart.push(product); // Add the product to the cart
    localStorage.setItem("cart", JSON.stringify(cart)); // Save updated cart back to localStorage

    alert(`${product.name} has been added to your cart!`);
}
document.getElementById("clear-cart").addEventListener("click", () => {
    localStorage.removeItem("cart"); // Clear the cart from localStorage
    // alert("Cart has been cleared.");
    loadCart(); // Refresh the cart display
});
