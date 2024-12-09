#ifndef INVENTORY_H
#define INVENTORY_H
#include <string>
#include "Product.h"
#include <list>
#include "Exception.h"

using std::string;
using std::list;

class Inventory {
public:
    // Delete copy constructor and assignment operator to prevent copying
    Inventory(const Inventory&) = delete;
    Inventory& operator=(const Inventory&) = delete;

    // Singleton access method
    static Inventory& getInstance();

    // buy product follow product id
    Product purchaseProduct(int id, int quantity);

    // Add product to inventory
    const Product& addProduct(Product& product);

    //Get all products
    const list<Product>& getAllProducts() const;

    //find product by id
    const Product& findProductById(int id) const;

    //Reset all products
    void reset();

private:
    // Private constructor to prevent direct instantiation
    Inventory() = default;

    // The single instance of the Inventory
    static Inventory* instance;

    static int lastProductID;

    list<Product> products;
};

#endif //INVENTORY_H