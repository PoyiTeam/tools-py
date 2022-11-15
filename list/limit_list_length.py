class CustomList(list):
    """
    Properties:
        blablabla
    Limitation: max length is 3
    """

    def __init__(self):
        self.max_len = 3

    def append(self, item):
        if len(self) < self.max_len:
            super().append(item)
        else:
            raise BaseException(
                f'Too many elements. {self.__class__.__name__} max length is {self.max_len} ')
