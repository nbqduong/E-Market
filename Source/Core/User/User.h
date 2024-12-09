#ifndef USER_H
#define USER_H
#include <string>
#include "Inventory.h"
using std::string;

class User{
public:
    User(const std::string& name, const std::string& email, const std::string& password);
    const string& getName();
    int getID();
    const string& getEmail();
    bool changePassword(const string& newPassword);

    void setAddress(const string& newAddress);

    static void reset();
protected:
    string m_name;
    static int m_id;
    string m_email;
    string m_password;
    string m_address;
};


#endif