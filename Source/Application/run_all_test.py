import unittest
import sys
import io
from user import Inventory, User

def run_all_tests():
    # Discover all test cases in the current directory
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test*.py')

    # Open a file to capture the output
    with open('test_results.txt', 'w') as result_file:
        # Create an in-memory string buffer to capture the output of each test run
        result_buffer = io.StringIO()

        # Create a TextTestRunner with the buffer to capture output
        runner = unittest.TextTestRunner(stream=result_buffer, verbosity=2)

        # Run the tests for each test file individually and reset after each file
        for test_suite in suite:
            # Run the test suite
            result = runner.run(test_suite)

            # Write the result from the buffer to the file
            result_file.write(result_buffer.getvalue())

            # Reset the buffer for the next test suite
            result_buffer.truncate(0)
            result_buffer.seek(0)

            # Reset the Inventory singleton state and User class after running the test suite
            Inventory.getInstance().reset()
            User.reset()

            # Check for failures or errors and exit with appropriate code if needed
            if not result.wasSuccessful():
                result_file.write("\nSome tests failed or had errors.\n")
                sys.exit(1)  # Exit with a non-zero status code to indicate failure

        # If all tests passed, write success message to file
        result_file.write("\nAll tests passed successfully.\n")
        sys.exit(0)  # Exit with zero status code to indicate success

if __name__ == "__main__":
    run_all_tests()
