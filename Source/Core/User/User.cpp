#include "User.h"

User::User(const std::string& name, const std::string& email, const std::string& password)
    : m_name(name), m_email(email), m_password(password) {}

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