import logging
import sys
import os

class MyLogger(object):

    def get_my_logger(app_home, prog_name):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        log_format = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s")

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(log_format)
        logger.addHandler(stdout_handler)

        file_handler = logging.FileHandler(os.path.join(app_home, "log", prog_name + ".log"), "a+")
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

        return logger
