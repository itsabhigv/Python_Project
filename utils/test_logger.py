class TestLogger:
    def log_success(self, reg, result):
        print(f"SUCCESS: {reg} => {result}")

    def log_failure(self, reg, message):
        print(f"FAILURE: {reg} => {message}")
