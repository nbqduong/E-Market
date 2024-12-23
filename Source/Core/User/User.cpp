#include "User.h"

int User::m_id = 0;

User::User(const std::string& name, const std::string& email, const std::string& password)
    : m_name(name), m_email(email), m_password(password) {m_id++;}

const std::string& User::getName(){
    return m_name;
}

int User::getID(){
    return m_id;
}

const string& User::getEmail(){
    return m_email;
}
bool User::changePassword(const string& newPassword){
    m_password = newPassword;
    return m_password != newPassword;
}

void User::reset(){
    m_id = 0;
}

void User::setAddress(const string& newAddress){
    m_address = newAddress;
}

