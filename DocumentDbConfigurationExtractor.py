import configparser
from DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager import documentDbConnectionDetails

def LoadDbCoonectionDetails():

    config = configparser.ConfigParser()
    configFile = config.read('Config.ini')
    documentDbConnectionDetails.documentdkey = config['DocumentDbConnectionDetails']['key']
    documentDbConnectionDetails.documentdburi = config['DocumentDbConnectionDetails']['uri']
    documentDbConnectionDetails.collectionname = config['DocumentDbConnectionDetails']['CollectionName']
    documentDbConnectionDetails.dbname = config['DocumentDbConnectionDetails']['DbName']

