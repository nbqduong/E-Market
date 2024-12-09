#ifndef PRODUCT_H
#define PRODUCT_H
#include <string>
using std::string;

class Product{
public:
    Product(int shopid, int id, string name, int price, int quantity, double star, int rate, string description);
    
    int getId() const;
    void setId(int id);
    const string& getName() const;
    int getPrice() const;
    int getQuantity() const;

    void setQuantity(int quantity);
    double getStar() const;
    int getRate() const;
    const string& getDescription() const;

    int getShopID() const;
  
private:
    int m_id;
    int m_shopId;

    string m_name;
    int m_price;
    int m_quantity;
    double m_star;
    int m_rate;

    string m_description;
    
    
};


#endif