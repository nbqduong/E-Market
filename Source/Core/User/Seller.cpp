#include "Seller.h"
const Product& Seller::getProduct(const string& name){
    return m_shop.getProduct(name);
}

list<Product>& Seller::getAllProducts(){
    return m_shop.getAllProducts();
}

void Seller::addProductToShop(const string& name, const int& price, const int& quantity, const string& description){
    m_shop.addProduct(name, price, quantity, description);
}
