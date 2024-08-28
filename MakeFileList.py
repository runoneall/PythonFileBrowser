import os
import Config

def GetRootList(id_:int) -> list:
    FolderPath = Config.GetPathWithId(id_)
    Items = os.listdir(FolderPath)
    rep_dict = dict()
    rep_dict['item'] = list()
    for item in Items:
        if os.path.isfile(f'{FolderPath}/{item}'):
            rep_dict['item'].append(
                {'name': item, 'type': 'file', 'path': f'/file-action/overview/{FolderPath}/{item}'}
            )
        else:
            rep_dict['item'].append(
                {'name': item, 'type': 'dir', 'path': f'/file-online/{id_}/{item}'}
            )
    rep_dict['updir'] = f'/file-online/{id_}'
    return rep_dict

def GetList(id_:int, path_:str) -> list:
    FolderPath = Config.GetPathWithId(id_)
    FolderPath = f'{FolderPath}/{path_}'
    Items = os.listdir(FolderPath)
    rep_dict = dict()
    rep_dict['item'] = list()
    for item in Items:
        if os.path.isfile(f'{FolderPath}/{item}'):
            rep_dict['item'].append(
                {'name': item, 'type': 'file', 'path': f'/file-action/overview/{FolderPath}/{item}'}
            )
        else:
            rep_dict['item'].append(
                {'name': item, 'type': 'dir', 'path': f'/file-online/{id_}/{path_}/{item}'}
            )
    rep_dict['updir'] = f'/file-online/{id_}/{path_}'
    return rep_dict