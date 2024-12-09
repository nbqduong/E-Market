#include "Cart.h"

bool Cart::addToCart(int id, int quantity) {
    try {
        // Use Inventory singleton to get the product
        // This will throw an exception if product not found or insufficient quantity
        Product product = Inventory::getInstance().purchaseProduct(id, quantity);
        
        // If successful, add the product to cart
        product.setQuantity(quantity);
        m_products.push_back(product);
        
        return true;
    }
    catch (const Exception& e) {
        // If an exception is thrown (product not found or insufficient quantity)
        // Return false to indicate failure
        return false;
    }
}

const list<Product>& Cart::getProducts() const{
    return m_products;
}