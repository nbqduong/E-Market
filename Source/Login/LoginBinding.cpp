#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Login.h"

namespace py = pybind11;

PYBIND11_MODULE(login, m) {
    py::class_<LoginManager>(m, "LoginManager")
        .def(py::init<>())  // Default constructor
        .def("validateCredentials", &LoginManager::validateCredentials, 
             py::arg("username"), py::arg("password"),
             "Validate user credentials")
        .def("registerUser", &LoginManager::registerUser, 
             py::arg("username"), py::arg("password"),
             "Register a new user");
}
