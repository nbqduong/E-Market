import unittest
import sys
import io
from user import Inventory, User

class OutputCapture:
    def __init__(self, file):
        self.file = file
        self.stdout = sys.stdout

    def write(self, message):
        # Write to the file
        self.file.write(message)
        # Print to the console
        self.stdout.write(message)

    def flush(self):
        # This is needed to ensure output is written immediately
        self.file.flush()
        self.stdout.flush()

def run_all_tests():
    # Discover all test cases in the current directory
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test*.py')

    # Open a file to capture the output
    with open('test_results.txt', 'w') as result_file:
        # Create an instance of OutputCapture to capture and redirect the output
        output_capture = OutputCapture(result_file)

        # Create a TextTestRunner with the output_capture to write to both file and console
        runner = unittest.TextTestRunner(stream=output_capture, verbosity=2)

        # Run the tests for each test file individually and reset after each file
        for test_suite in suite:
            # Run the test suite
            result = runner.run(test_suite)

            # Reset the Inventory singleton state and User class after running the test suite
            Inventory.getInstance().reset()
            User.reset()

            # Check for failures or errors and exit with appropriate code if needed
            if not result.wasSuccessful():
                result_file.write("\nSome tests failed or had errors.\n")
                sys.exit(1)  # Exit with a non-zero status code to indicate failure

        # If all tests passed, write success message to file and print to console
        result_file.write("\nAll tests passed successfully.\n")
        sys.exit(0)  # Exit with zero status code to indicate success

if __name__ == "__main__":
    run_all_tests()
