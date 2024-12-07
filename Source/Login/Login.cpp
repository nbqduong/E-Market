#include "Login.h"

LoginManager::LoginStatus LoginManager::validateCredentials(const std::string& username, const std::string& password){
    return LoginStatus::CUSTOMER;
}