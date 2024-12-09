#include "Customer.h"

const string Customer::getAddress(){
    return "test address";
}

void Customer::addToCart(int id, int amount){
    m_cart.addToCart(id, amount);
}

const list<Product>& Customer::getAllCartItems() const{
    return m_cart.getProducts();
}