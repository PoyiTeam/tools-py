import os
import inspect


def get_func_name(func):
    module_name = os.path.basename(inspect.stack()[0][1])
    func_name = inspect.getmembers(func, inspect.isfunction)[0][1]
    print(get_func_name)
    return f'module: {module_name}, {func_name}'


class myclass:
    def __init__(self) -> None:
        print(get_func_name(self.__init__))


myclass()
