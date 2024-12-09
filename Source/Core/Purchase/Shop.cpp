#include "Shop.h"

// Initialize the static shop ID
int Shop::m_id = 0;

// Default constructor increments the shop ID
Shop::Shop() {
    std::cout << "Shop constructor Debug" << std::endl;
    m_id++; // Increment static shop ID for each new shop
}

bool Shop::addProduct(const string& name, const int& price, const int& quantity, const string& description) {
    try {
        // Create a new Product with the shop's ID
        // Note the order of constructor parameters: (shopid, id, name, price, quantity, star, rate, description)
        Product newProduct(
            m_id,      // Shop ID 
            0,         // ID will be set by Inventory
            name, 
            price, 
            quantity, 
            0.0,       // Default star rating 
            0,         // Default rate
            description
        );
        
        // Use Inventory's addProduct method
        // This will set the product ID and add it to the inventory
        const Product& addedProduct = Inventory::getInstance().addProduct(newProduct);
        
        // Add the product to the shop's local product list
        products.push_back(addedProduct);
        
        return true;
    }
    catch (const Exception& e) {
        // If an exception occurs during product addition
        return false;
    }
}