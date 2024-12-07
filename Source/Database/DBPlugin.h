#ifndef DBPLUGIN_H
#define DBPLUGIN_H

#include <string>

class DBPlugin {
public:
    // Constructor
    DBPlugin(const std::string& dbName, const std::string& user, const std::string& password, 
             const std::string& host, int port);

    // Getters
    std::string getDBName() const;
    std::string getUser() const;
    std::string getPassword() const;
    std::string getHost() const;
    int getPort() const;

    // Setters
    void setDBName(const std::string& dbName);
    void setUser(const std::string& user);
    void setPassword(const std::string& password);
    void setHost(const std::string& host);
    void setPort(int port);

private:
    std::string dbName;
    std::string user;
    std::string password;
    std::string host;
    int port;
};

#endif // DBPLUGIN_H