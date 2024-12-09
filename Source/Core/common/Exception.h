#ifndef EXCEPTION_H
#define EXCEPTION_H

#include <string>
#include <string_view>

using std::string;
using std::string_view;

class Exception
{
public:
    explicit Exception(string_view msg) : msg_{msg} { }
    const string& what() const { return msg_; }

private:
    string msg_;
};

#endif //EXCEPTION_H