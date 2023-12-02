import logging
import os

# Construct the path to the log file using os.path
log_file_path = os.path.join('logs', 'automation.log')

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

# Create a logger instance
logger = logging.getLogger()