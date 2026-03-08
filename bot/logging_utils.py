import logging

#This sets up a one time log file
def setup_logger():
    logging.basicConfig(
        filename='logs.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

#Everytime the order is placed the logs will be saved to the log file created above
def log_info(message):
    logging.info(message)

#Everytime an error occurs the log of it will be saved in the log file created above
def log_error(message):
    logging.error(message)

