import json

def LoadConfig(ConfigName:str) -> dict:
    ConfigFilePath = f'./Resource/{ConfigName}.json'
    with open(ConfigFilePath, 'r', encoding='utf-8') as ConfigFile:
        ConfigDict = json.load(ConfigFile)
    return ConfigDict

def UserConfig() -> dict:
    ConfigDict = LoadConfig('users')
    UserList = list(ConfigDict.keys())

def FolderConfig() -> list[dict]:
    FolderList = LoadConfig('folders')
    return FolderList

def PathWithId(id_:int) -> dict:
    for OneFolder in FolderConfig():
        if OneFolder['id'] == id_:
            return OneFolder