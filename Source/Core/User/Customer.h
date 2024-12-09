#ifndef CUSTOMER_H
#define CUSTOMER_H
#include <string>
#include <iostream>
#include "User.h"
using std::string;

class Customer: public User{
    
public:
    Customer(const std::string& name, const std::string& email, const std::string& password)
    :User(name,email,password){
        std::cout << "Customer constructor debugging" << std::endl;
    }
    const string getAddress();
private:
    //cart
    //purchase history
    //address
};

#endif