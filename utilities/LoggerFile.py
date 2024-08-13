import logging  # Import the logging module to enable logging functionality
import inspect  # Import the inspect module to retrieve the current stack frame

class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]  # Get the name of the function that called loggen()
        logger = logging.getLogger(name)  # Create a logger object with the caller's name
        logfile = logging.FileHandler(".\\Logs\\OrageHRM_Log.log")  # Create a file handler to write logs to a file
        logformat = logging.Formatter(
            "%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s : %(lineno)d : %(message)s"
        )  # Define the format for the log messages
        logfile.setFormatter(logformat)  # Set the defined format to the file handler
        logger.addHandler(logfile)  # Add the file handler to the logger
        logger.setLevel(logging.INFO)  # Set the logging level to INFO
        return logger  # Return the configured logger object

    # The following comments describe the logging configuration and different log levels:

    # get log ==> logging.getLogger()  # Retrieve a logger object
    # logfile ==> log file path  # Path where the log file is stored
    # logformat ==> logs format  # Format of the log messages
    # setformatter ==> link file and format  # Associate the format with the file handler
    # add handler --> maintain all logs every time in log file  # Ensure logs are written to the file

    # debug  # Detailed information for diagnosing problems
    # info  # General information about program execution
    # warnings  # Indications of potential problems
    # error  # Errors that occur during program execution
    # critical  # Severe errors that cause premature termination
