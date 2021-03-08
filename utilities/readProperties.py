# reads the common data
import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod # Methods can be accessed with creating an object
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod # Methods can be accessed with creating an object
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod # Methods can be accessed with creating an object
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod  # Methods can be accessed with creating an object
    def getName():
        name = config.get('common info', 'name')
        return name

    @staticmethod  # Methods can be accessed with creating an object
    def getDescription():
        description = config.get('common info', 'description')
        return description

    @staticmethod  # Methods can be accessed with creating an object
    def setNationality(name):
        config.set('common info', 'name', name)

    @staticmethod  # Methods can be accessed with creating an object
    def setDescription(description):
        config.set('common info', 'description', description)