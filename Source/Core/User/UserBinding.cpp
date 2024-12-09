#include <pybind11/pybind11.h>
#include "User.h"
#include "Admin.h"
#include "Customer.h"
#include "Seller.h"
#include "Shop.h"

namespace py = pybind11;

PYBIND11_MODULE(user, m) {
    // Bind User class
    py::class_<User>(m, "User")
        .def(py::init<const std::string&, const std::string&, const std::string&>())
        .def("getName", &User::getName)
        .def("getID", &User::getID)
        .def("getEmail", &User::getEmail)
        .def("changePassword", &User::changePassword);

    // // Bind Admin class
    // py::class_<Admin, User>(m, "Admin")
    //     .def(py::init<const std::string&, const std::string&, const std::string&>());

    // Bind Customer class
    py::class_<Customer, User>(m, "Customer")
        .def(py::init<const std::string&, const std::string&, const std::string&>())
        .def("getAddress", &Customer::getAddress);

    // Bind Seller class
    py::class_<Seller, User>(m, "Seller")
        .def(py::init<const std::string&, const std::string&, const std::string&>())
        .def("testfunc", &Seller::testfunc);


    py::class_<Shop>(m, "Shop")
        // Bind the default constructor
        .def(py::init<>())
        
        // Bind the addProduct method
        .def("addProduct", &Shop::addProduct, 
             "Add a product to the shop", 
             py::arg("name"), 
             py::arg("price"), 
             py::arg("quantity"), 
             py::arg("description"))
        
        // Bind the test method
        .def("test", &Shop::test, 
             "Test function for Shop class");
}