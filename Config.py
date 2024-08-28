import json

def LoadConfig(ConfigName:str) -> dict:
    ConfigFilePath = f'./Resource/{ConfigName}.json'
    with open(ConfigFilePath, 'r', encoding='utf-8') as ConfigFile:
        ConfigDict = json.load(ConfigFile)
    return ConfigDict

def LoadUserConfig() -> dict:
    ConfigDict = LoadConfig('users')
    UserList = list(ConfigDict.keys())

def LoadGlobalConfig() -> dict:
    GlobalDict = LoadConfig('global')