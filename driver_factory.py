from utils.log_utility import LogUtility


class DriverFactory:

    def __int__(self):
        self.driver = None
        self.log = LogUtility()

    def get_driver(self, driver_name):
        self.log.info(f"Getting driver for {driver_name}")
