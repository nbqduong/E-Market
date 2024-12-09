#include "Cart.h"

bool Cart::addToCart(int id, int quantity) {
    try {
        // Use Inventory singleton to get the product
        // This will throw an exception if product not found or insufficient quantity
        const Product& product = Inventory::getInstance().getProduct(id, quantity);
        
        // If successful, add the product to cart
        products.push_back(product);
        
        return true;
    }
    catch (const Exception& e) {
        // If an exception is thrown (product not found or insufficient quantity)
        // Return false to indicate failure
        return false;
    }
}