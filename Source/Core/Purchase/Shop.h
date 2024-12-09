#ifndef SHOP_H
#define SHOP_H
#include <string>
#include "Inventory.h"
#include <list>
#include "Exception.h"

using std::string;
using std::list;

class Shop{
public:
    //Constructor

    //Use Inventory's method to implement this method
    bool addProduct(const string& name, const int & price, const int & quantity, const string& description);
    
  
private:
    list<Product> products;
    string m_name;
    static int m_id;
};


#endif