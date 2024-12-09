#ifndef CART_H
#define CART_H
#include <string>
#include "Inventory.h"
#include <list>
#include "Exception.h"

using std::string;
using std::list;

class Cart{
public:
    //Use Inventory's method to implement this method
    bool addToCart(int id, int quantity);
    
  
private:
    list<Product> products;
};


#endif