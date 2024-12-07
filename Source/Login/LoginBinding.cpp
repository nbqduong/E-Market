#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Login.h"

namespace py = pybind11;

PYBIND11_MODULE(login, m) {
    py::enum_<LoginManager::LoginStatus>(m, "LoginStatus")
        .value("CUSTOMER", LoginManager::LoginStatus::CUSTOMER)
        .value("SELLER", LoginManager::LoginStatus::SELLER)
        .value("ADMIN", LoginManager::LoginStatus::ADMIN)
        .value("INCORRECT", LoginManager::LoginStatus::INCORRECT)
        .value("DB_ERROR", LoginManager::LoginStatus::DB_ERROR)
        .export_values();

    // Binding the LoginManager class
    py::class_<LoginManager>(m, "LoginManager")
        .def(py::init<>())  // Default constructor
        .def("validateCredentials", &LoginManager::validateCredentials)
        .def("registerUser", &LoginManager::registerUser);
}
