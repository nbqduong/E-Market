import unittest
from user import Customer, Seller, Inventory

class TestECommerceSystem(unittest.TestCase):

    def setUp(self):
        # Reset the Inventory singleton and initialize test data before each test
        Inventory.getInstance().reset()

    def test_customer_cart_and_inventory(self):
        # Create a Seller and add products to the shop
        seller = Seller("Jane din", "jane@example.com", "testpassword")
        seller.addProductToShop("test_product", 20, 10, "add product for testing")
        seller.addProductToShop("test_product2", 300, 10, "add product for testing2")

        # Create a Customer
        customer = Customer("Jane Doe", "jane@example.com", "testpassword")

        # Get the inventory instance and list all products
        invent = Inventory.getInstance()
        products = list(invent.getAllProducts())

        # Add 2 units of "test_product2" to the customer's cart
        item1_id = products[1].getId()
        customer.addToCart(item1_id, 2)

        # Check the remaining stock of "test_product2"
        products = list(invent.getAllProducts())
        self.assertEqual(products[1].getQuantity(), 8, "Remaining stock of test_product2 should be 8")

        # Verify the customer's cart for "test_product2"
        cart_items = list(customer.getAllCartItems())
        self.assertEqual(cart_items[0].getName(), "test_product2", "First item name in cart should be test_product2")
        self.assertEqual(cart_items[0].getQuantity(), 2, "Quantity of test_product2 in cart should be 2")
        self.assertEqual(cart_items[0].getPrice(), 300, "Price of test_product2 in cart should be 300")

        # Add 5 units of "test_product" to the customer's cart
        item2_id = products[0].getId()
        customer.addToCart(item2_id, 5)

        # Check the remaining stock of "test_product"
        products = list(invent.getAllProducts())
        self.assertEqual(products[0].getQuantity(), 5, "Remaining stock of test_product should be 5")

        # Verify the customer's cart for both products
        cart_items = list(customer.getAllCartItems())
        self.assertEqual(cart_items[0].getName(), "test_product2", "First item name in cart should be test_product2")
        self.assertEqual(cart_items[0].getQuantity(), 2, "Quantity of test_product2 in cart should be 2")
        self.assertEqual(cart_items[0].getPrice(), 300, "Price of test_product2 in cart should be 300")

        self.assertEqual(cart_items[1].getName(), "test_product", "Second item name in cart should be test_product")
        self.assertEqual(cart_items[1].getQuantity(), 5, "Quantity of test_product in cart should be 5")
        self.assertEqual(cart_items[1].getPrice(), 20, "Price of test_product in cart should be 20")

if __name__ == "__main__":
    unittest.main()
