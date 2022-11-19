import pathlib
import os


def GetEntrancePath():
    script_direction = str(pathlib.Path(__file__).parent.resolve()) + "/"
    return script_direction


def GetFolderDirection(folder_path, folder_content):
    folder_paths = []
    i = 0
    for item in folder_content:
        path = folder_path + item + "/"
        if os.path.isdir(path):
            folder_paths.append(path)
            i += 1

    return folder_paths