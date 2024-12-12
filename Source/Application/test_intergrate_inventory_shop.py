import unittest
from user import Seller, Product, Inventory

class TestSellerModule(unittest.TestCase):

    def setUp(self):
        """Set up a Seller instance before each test."""
        self.seller = Seller("Jane din", "jane@example.com", "testpassword")
        self.seller.addProductToShop("test_product", 20, 10, "add product for testing")
        self.inventory = Inventory.getInstance()

    def test_add_product_to_shop(self):
        """Test adding a product to the shop."""
        products = list(self.seller.getAllProducts())
        # test init list product
        p = list(self.inventory.getAllProducts())
        self.assertEqual(len(products), 1, "Product count mismatch after adding.")
        self.assertEqual(products[0].getDescription(), "add product for testing", "Product description mismatch.")
        self.assertEqual(p[0].getDescription(), "add product for testing", "Product description mismatch with inventory.")

        #add more items to inventory
        self.seller.addProductToShop("test_product1", 20, 10, "add product for testing1")
        self.seller.addProductToShop("test_product2", 30, 10, "add product for testing2")

        #test after adding product
        p = list(self.inventory.getAllProducts())
        self.assertEqual(p[1].getDescription(), "add product for testing1", "Product description mismatch with inventory.")
        self.assertEqual(p[2].getDescription(), "add product for testing2", "Product description mismatch with inventory.")
        self.assertEqual(p[1].getPrice(), 20, "Product description mismatch with inventory.")
        self.assertEqual(p[2].getPrice(), 30, "Product description mismatch with inventory.")

    def test_get_product_by_name(self):
        """Test retrieving a product by its name."""
        product = self.seller.getProduct("test_product")
        self.assertIsNotNone(product, "Product not found.")
        self.assertEqual(product.getPrice(), 20, "Product price mismatch.")
        self.assertEqual(product.getQuantity(), 10, "Product quantity mismatch.")
        self.assertEqual(product.getDescription(), "add product for testing", "Product description mismatch.")

if __name__ == "__main__":
    unittest.main()

