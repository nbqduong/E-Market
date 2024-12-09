#include "Inventory.h"

// Initialize the static instance pointer to nullptr
Inventory* Inventory::instance = nullptr;

int Inventory::lastProductID = 0;

// Singleton getInstance method
Inventory& Inventory::getInstance() {
    // Implement Meyers' Singleton (thread-safe in C++11 and later)
    static Inventory instance;
    return instance;
}

Product Inventory::purchaseProduct(int id, int quantity) {
    // Iterate through the products list to find the product with matching id
    for (auto& product : products) {
        if (product.getId() == id) {
            // Check if the requested quantity is available
            if (product.getQuantity() >= quantity) {
                // Reduce the product quantity
                const_cast<Product&>(product) = Product(
                    product.getShopID(),
                    product.getId(), 
                    product.getName(), 
                    product.getPrice(), 
                    product.getQuantity() - quantity, 
                    product.getStar(), 
                    product.getRate(), 
                    product.getDescription()
                );
                return product;
            }
            else {
                // If not enough quantity, throw an exception
                throw Exception("Not enough quantity available for product");
            }
        }
    }
    
    // If no product with the given id is found, throw an exception
    throw Exception("Product not found in inventory");
}

const Product& Inventory::addProduct(Product& product) {
    // Check if a product with the same id already exists
    for (auto& existingProduct : products) {
        if (existingProduct.getShopID() == product.getShopID() && existingProduct.getName() == product.getName()) {
            // If product exists, update its quantity
            const_cast<Product&>(existingProduct) = Product(
                existingProduct.getShopID(),
                existingProduct.getId(), 
                existingProduct.getName(), 
                existingProduct.getPrice(), 
                existingProduct.getQuantity() + product.getQuantity(), 
                existingProduct.getStar(), 
                existingProduct.getRate(), 
                existingProduct.getDescription()
            );
            return existingProduct;
        }
    }
    
    // If product doesn't exist, add it to the list
    lastProductID++;
    product.setId(lastProductID);
    products.push_back(product);
    return product;
}

const list<Product>& Inventory::getAllProducts() const{
    return products;
}

void Inventory::reset(){
    products.clear();
    lastProductID = 0;
}

const Product& Inventory::findProductById(int id) const {
    for (auto& product : products) {
        if (product.getId() == id) {
            return product;
        }
    }
}