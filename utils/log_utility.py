from datetime import datetime


class LogUtility:

    def __init__(self):
        self.RED = "\033[91m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.CYAN = "\033[96m"
        self.RESET = "\033[0m"

        self.date_format = "%Y-%m-%d %H:%M:%S"

    def debug(self, msg):
        print(f"{self.YELLOW} [DEBUG] {msg} {self.RESET}")

    def error(self, msg):
        print(f"{self.RED} [ERROR] {msg} {self.RESET}")

    def info(self, msg):
        print(f"{self.GREEN} [INFO] {msg} {self.RESET}")

    def warn(self, msg):
        print(f"{self.CYAN} [WARN] {msg} {self.RESET}")

    def __now(self):
        return datetime.now().strftime(self.date_format)


if __name__ == '__main__':
    logger = LogUtility()
    logger.info("This is an info message")
    logger.debug("This is a debug message")
    logger.error("This is an error message")
    logger.warn("This is a warning message")
