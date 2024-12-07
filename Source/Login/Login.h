#ifndef LOGIN_MANAGER_H
#define LOGIN_MANAGER_H

#include <string>

class LoginManager {
public:
    bool validateCredentials(const std::string& username, const std::string& password);
    void registerUser(const std::string& username, const std::string& password){};
};

#endif // LOGIN_MANAGER_H

