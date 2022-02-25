#Writing logs to files
import logging
import logging.handlers
from pathlib import Path

""" 
Set up logging
Ensure that all messages can be handled on the output stream
To quiet different levels in the logs, we will quiet the specific logger,
not the whole stream
"""
handlerPrint = logging.StreamHandler()

# Allow everything to be printed
handlerPrint.setLevel(logging.DEBUG)

# Make new log every hour with 23 backups for the other hours
log_dir = "./log_files/"
# Ensure directory exists
Path(log_dir).mkdir(parents=True, exist_ok=True)
log_fname = "logger.log"
handlerWrite = logging.handlers.TimedRotatingFileHandler(
    log_dir + log_fname,
    when="h",
    interval=1, # Every hour, a new file will be created
    backupCount=23) #A maximum of 24 files will exist. After this, logs will be overwritten.

# Allow everything to be printed
handlerWrite.setLevel(logging.DEBUG)

# Set up the formatter globally
formatter = logging.Formatter('%(asctime)25.25s | %(levelname)10.10s | %(filename)20.20s | %(message)s')
handlerPrint.setFormatter(formatter)
handlerWrite.setFormatter(formatter)

# Common method to create a logger
def setup_logger(name):

    # A logger with name my_logger will be created
    # and then add it to the print stream
    log = logging.getLogger(name)
    
    # Turn on INFO by default
    # Leave DEBUG for developers
    log.setLevel(logging.DEBUG)
    
    # Add logger to the handlers
    log.addHandler(handlerPrint)
    log.addHandler(handlerWrite)

    return log
