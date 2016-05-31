class TaskModel:

    '''constructor'''
    def __init__(self, title):
        if type(title) is not str or title == "":
            raise Exception("title is not a string")
        '''Private attributes'''
        self.__title = title
        self.__callback_title = None

    '''getter & setter'''
    def get_title(self):
        return self.__title
    def set_callback_title(self, callback_title):
        self.__callback_title = callback_title

    ''' reverse title'''
    def toggle(self):
        self.__title = self.__title[::-1]
        self.__callback_title(self.__title)

    ''' return value str'''
    def __str__(self):
        return self.__title
