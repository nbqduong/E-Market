#ifndef CUSTOMER_H
#define CUSTOMER_H
#include <string>
#include <iostream>
#include "User.h"
#include "Cart.h"
using std::string;

class Customer: public User{
    
public:
    Customer(const std::string& name, const std::string& email, const std::string& password)
    :User(name,email,password){
        std::cout << "Customer constructor debugging" << std::endl;
    }
    const string getAddress();
    void addToCart(int id, int amount);

    const list<Product>& getAllCartItems() const;
private:
    //cart
    Cart m_cart; //cart
    //purchase history

};

#endif