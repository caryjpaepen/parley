import logging
import time
import logging
import time

def configure_logger():
    timestamp = int(time.time())
    
    # Create a logger
    logger = logging.getLogger("parley")
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler
    file_handler = logging.FileHandler(f'parley_{timestamp}.log')
    file_handler.setLevel(logging.DEBUG)
    
    # Create a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    
    # Set the formatter for both handlers
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)