#ifndef SHOP_H
#define SHOP_H
#include <string>
#include "Inventory.h"
#include <list>
#include <iostream>
#include "Exception.h"

using std::string;
using std::list;

class Shop{
public:
    //Constructor
    Shop();

    //Use Inventory's method to implement this method
    bool addProduct(const string& name, const int & price, const int & quantity, const string& description);

    void test(){
        std::cout << "test fucntion from shop" << std::endl;
    }
    
  
private:
    list<Product> products;
    string m_name;
    static int m_id;
};


#endif