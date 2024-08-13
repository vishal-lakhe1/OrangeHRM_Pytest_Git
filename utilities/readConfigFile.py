import configparser  # Import the configparser module to handle configuration files

config = configparser.RawConfigParser()  # Create a RawConfigParser object
config.read(".\\Configuration\\config.ini")  # Read the configuration file

class ReadConfig_Class:

    @staticmethod
    def getUsername():
        Username = config.get('login data', 'username')  # Retrieve the username from the configuration file
        return Username  # Return the username

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')  # Retrieve the password from the configuration file
        return Password  # Return the password
