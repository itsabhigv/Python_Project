import re
from utils.file_handler import FileHandler
from utils.car_valuation import CarValuation
from utils.test_logger import TestLogger

# File paths
INPUT_FILE = "car_input.txt"
OUTPUT_FILE = "car_output.txt"

class TestAutomationSuite:
    def __init__(self):
        self.file_handler = FileHandler()
        self.car_valuation = CarValuation()
        self.logger = TestLogger()

    def extract_registration_numbers(self, text):
        """Extract registration numbers from text using regex patterns."""
        pattern = r"[A-Z]{2}\d{2}[A-Z]{3}"  # Registration pattern (e.g., AD58VNF)
        return re.findall(pattern, text)

    def run_tests(self):
        # Step 1: Read input file
        input_text = self.file_handler.read_file(INPUT_FILE)
        reg_numbers = self.extract_registration_numbers(input_text)
        # Step 2: Load expected output data
        expected_data = self.file_handler.read_csv(OUTPUT_FILE)
        # Step 3 & 4: Iterate through registrations, perform valuation, and validate
        for reg in reg_numbers:
            try:
                result = self.car_valuation.fetch_valuation(reg)
                expected = expected_data.get(reg)

                if not expected:
                    self.logger.log_failure(reg, "No expected data found.")
                    continue

                # Compare result with expected
                if result == expected:
                    self.logger.log_success(reg, result)
                else:
                    self.logger.log_failure(reg, f"Mismatch: Expected {expected}, Got {result}")
            except Exception as e:
                self.logger.log_failure(reg, f"Error occurred: {e}")

if __name__ == "__main__":
    suite = TestAutomationSuite()
    suite.run_tests()

