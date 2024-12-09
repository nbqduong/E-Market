#include "Product.h"

// Constructor implementation
Product::Product(int shopid, int id, string name, int price, int quantity, double star, int rate, string description)
    : m_shopId(shopid),
      m_id(id), 
      m_name(name), 
      m_price(price), 
      m_quantity(quantity), 
      m_star(star), 
      m_rate(rate), 
      m_description(description) 
{
    // Constructor body is empty as initialization is done via member initializer list
}

// Getter implementations
int Product::getId() const {
    return m_id;
}

const string& Product::getName() const {
    return m_name;
}

int Product::getPrice() const {
    return m_price;
}

int Product::getQuantity() const {
    return m_quantity;
}

double Product::getStar() const {
    return m_star;
}

int Product::getRate() const {
    return m_rate;
}

const string& Product::getDescription() const {
    return m_description;
}

int Product::getShopID() const {
    return m_shopId;
}

void Product::setId(int id){
    m_id = id;
}