#ifndef CUSTOMER_H
#define CUSTOMER_H
#include <string>
#include "User.h"
using std::string;

class Customer: public User{
    
public:
    const string& getAddress();
private:
    //cart
    //purchase history
    //address
};

#endif