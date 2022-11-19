import pathlib
import os


def get_script_directory():
    directory = str(pathlib.Path(__file__).parent.resolve())
    directory = directory.replace(os.sep, "/") + "/"

    return directory


def get_child_directory(directory, directory_content):
    paths_folder = []
    i = 0
    for item in directory_content:
        path = directory + item + "/"
        if os.path.isdir(path):
            paths_folder.append(path)
            i += 1

    return paths_folder


def get_specific_extension(file_name, target_extension):
    """
    check if input file_name is same extension
    input: file_name, extension
    """
    print("file path:", file_name)
    name, extension = os.path.splitext(file_name)
    check_extension = extension == target_extension

    return check_extension


def directory_contents(directory):
    directory_contents = os.listdir(directory)
    return directory_contents
