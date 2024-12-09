import unittest
from user import User, Customer, Seller  # Assuming these are correctly imported from your module

class TestUserModule(unittest.TestCase):
    def test_customer_class(self):
        # Create an instance of Customer
        customer = Customer("Jane Doe", "jane@example.com", "testpassword")
        
        # Assert values
        self.assertEqual(customer.getName(), "Jane Doe", "Customer name does not match")
        self.assertEqual(customer.getID(), 1, "Customer ID does not match")
        self.assertEqual(customer.getEmail(), "jane@example.com", "Customer email does not match")
        
        # Test getAddress
        self.assertEqual(customer.getAddress(), "test address", "Customer address does not match")

    def test_seller_class(self):
        # Create an instance of Seller
        seller = Seller("Jane din", "jane@example.com", "testpassword")
        
        # Assert values
        self.assertEqual(seller.getName(), "Jane din", "Seller name does not match")
        self.assertEqual(seller.getID(), 2, "Seller ID does not match")
        self.assertEqual(seller.getEmail(), "jane@example.com", "Seller email does not match")

    def test_user_class(self):
        # Create an instance of User
        user = User("John Doe", "john@example.com", "connect")
        
        # Assert values
        self.assertEqual(user.getName(), "John Doe", "User name does not match")
        self.assertEqual(user.getID(), 3, "User ID does not match")
        self.assertEqual(user.getEmail(), "john@example.com", "User email does not match")
        
        # Test changing password
        user.changePassword("new_password")
        # Assuming no output or return from changePassword; no direct assert here


if __name__ == "__main__":
    # Run the tests
    unittest.main()
