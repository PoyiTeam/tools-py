"""
v.20220920
"""
import os
import glob
import re


def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]


def get_dirs(path):
    """
    path: path-like data

    return: list of directory under path
    """

    paths = list_full_paths(path)
    return [path for path in paths if os.path.isdir(path)]


def get_files(path):
    """
    path: path-like data

    return: list of files under path
    """

    paths = list_full_paths(path)
    return [path for path in paths if os.path.isfile(path)]


def get_specific_ext(paths, target_ext):
    """
    paths: array-like of path-like data
    target_ext: specific files extension

    return: list of specific extension file names
    """
    path_files = list()
    for path in paths:
        name, ext = os.path.splitext(path)
        if ext == target_ext:
            path_files.append(path)
    return path_files


# def walk_to_subdir(func, root, depth: int):
def walk_subpaths(root, depth):
    """
    Walk to specific depth from `root` and list all path
    `root`: path-like
        root directory
    `depth`: int
        specific how depth
        ex: `depth = 2`
            ----root
                |---subdir_1_1
                    |---subdir_1_2
                    |---hello.txt
                |---subdir_2_1
                    |---subdir_2_2
                    |---world.txt
            return a list contain all of the contents in `depth=2` from root.
    """
    subpath = root
    for i in range(depth):
        subpath = os.path.join(subpath, '*')
    return glob.glob(subpath)


def walk_subdirs(root, depth):
    """
    Walk to specific depth from `root` and list all directory
    `root`: path-like
        root directory
    `depth`: int
        specific how depth
        ex: `depth = 2`
            ----root
                |---subdir_1_1
                    |---subdir_1_2
                    |---hello.txt
                |---subdir_2_1
                    |---subdir_2_2
                    |---word.txt
            return a `filter` object contain [root/subdir_1_1/subdir_1_2, 
                                              root/subdir_2_1/subdir_2_2]
    """
    subpaths = walk_subpaths(root, depth-1)
    return list(filter(lambda f: os.path.isdir(f), subpaths))


def walk_files_specific_depth(root, depth):
    """
    Walk to specific depth from `root` and list all directory
    `root`: path-like
        root directory
    `depth`: int
        specific how depth
        ex: `depth = 2`
            ----root
                |---subdir_1_1
                    |---subdir_1_2
                    |---hello.txt
                |---subdir_2_1
                    |---subdir_2_2
                    |---world.txt
            return a `filter` object contain[root/subdir_1_1/hello.txt,
                                             root/subdir_2_1/world.txt]
    """
    subpaths = walk_subpaths(root, depth-1)
    return list(filter(lambda f: os.path.isfile(f), subpaths))


def get_specific_path_with_key(paths, key: str):
    """
    paths: array-like
    key: str
        keyword for searching
    """
    return [path for path in paths if key in os.path.basename(path)]
