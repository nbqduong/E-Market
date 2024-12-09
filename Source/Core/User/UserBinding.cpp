#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
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
        .def("changePassword", &User::changePassword)
        .def_static("reset", &User::reset)
        .def("setAddress", &User::setAddress);

    // // Bind Admin class
    // py::class_<Admin, User>(m, "Admin")
    //     .def(py::init<const std::string&, const std::string&, const std::string&>());

    // Bind Customer class
    py::class_<Customer, User>(m, "Customer")
        .def(py::init<const std::string&, const std::string&, const std::string&>())
        .def("getAddress", &Customer::getAddress)
        .def("addToCart", &Customer::addToCart)
        .def("getAllCartItems", &Customer::getAllCartItems);
        

    // Bind Seller class
    py::class_<Seller, User>(m, "Seller")
        // Bind the constructor
        .def(py::init<const std::string&, const std::string&, const std::string&>(), 
             py::arg("name"), 
             py::arg("email"), 
             py::arg("password"))
        
        // Bind method to add product to shop
        .def("addProductToShop", &Seller::addProductToShop, 
             "Add a product to the seller's shop",
             py::arg("name"), 
             py::arg("price"), 
             py::arg("quantity"), 
             py::arg("description"))

        // Bind method to get a specific product
        .def("getProduct", &Seller::getProduct, 
             "Get a product by name",
             py::arg("name"))
        
        // Bind method to get all products
        .def("getAllProducts", &Seller::getAllProducts, 
             "Get all products in the shop",
             py::return_value_policy::reference_internal);


    // Bind the Shop class
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
        
        // Bind the getProduct method
        .def("getProduct", &Shop::getProduct, 
             "Get a product by name",
             py::arg("name"))
        
        // Bind the getAllProducts method
        .def("getAllProducts", &Shop::getAllProducts, 
             "Get all products in the shop",
             py::return_value_policy::reference_internal);


    py::class_<Product>(m, "Product")
        // Bind the constructor
        .def(py::init<int, int, std::string, int, int, double, int, std::string>(), 
            py::arg("shopid"), 
            py::arg("id"), 
            py::arg("name"), 
            py::arg("price"), 
            py::arg("quantity"), 
            py::arg("star"), 
            py::arg("rate"), 
            py::arg("description"))
        
        // Bind getter methods
        .def("getId", &Product::getId, "Get the product ID")
        .def("setId", &Product::setId, "Set the product ID", py::arg("id"))
        .def("getName", &Product::getName, "Get the product name")
        .def("getPrice", &Product::getPrice, "Get the product price")
        .def("getQuantity", &Product::getQuantity, "Get the product quantity")
        .def("getStar", &Product::getStar, "Get the product star rating")
        .def("getRate", &Product::getRate, "Get the product rate")
        .def("getDescription", &Product::getDescription, "Get the product description")
        .def("getShopID", &Product::getShopID, "Get the shop ID");


            // Bind the Inventory class
    py::class_<Inventory>(m, "Inventory")
        .def_static("getInstance", &Inventory::getInstance, py::return_value_policy::reference)
        .def("purchaseProduct", &Inventory::purchaseProduct)
        .def("addProduct", &Inventory::addProduct)
        .def("getAllProducts", &Inventory::getAllProducts)
        .def("findProductById", &Inventory::findProductById)
        .def("reset", &Inventory::reset);
;
}