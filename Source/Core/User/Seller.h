#ifndef SELLER_H
#define SELLER_H
#include <string>
#include "User.h"
#include "Shop.h"

using std::string;

class Seller: public User{
    
public:
    Seller(const std::string& name, const std::string& email, const std::string& password)
    :User(name,email,password){
        std::cout << "Seller constructor debugging" << std::endl;
    }
    
    void addProductToShop(const string& name, const int& price, const int& quantity, const string& description);

    const Product& getProduct(const string& name);

    list<Product>& getAllProducts();
    
private:
    //shop
    Shop m_shop{};
    //sell history
    //address
};


#endif