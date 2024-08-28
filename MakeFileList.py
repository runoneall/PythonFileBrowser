import Config

def GetRootList(id_:int) -> list:
    FolderPath = Config.PathWithId(id_)
    return FolderPath

def GetList(id_:int, path_:str) -> list:
    pass