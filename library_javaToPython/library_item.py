class LibraryItem:
    def __init__(self, title, item_id):
        self.__title = title
        self.__item_id = item_id
        self.__checked_out = False

    def get_title(self):
        return self.__title

    def get_item_id(self):
        return self.__item_id

    def is_checked_out(self):
        return self.__checked_out

    def check_out(self):
        if not self.__checked_out:
            self.__checked_out = True
            return True
        return False

    def return_item(self):
        if self.__checked_out:
            self.__checked_out = False
            return True
        return False

    def __str__(self):
        return "Title: " + self.__title + "\nItem ID: " + self.__item_id + "\nChecked Out: " + str(self.__checked_out)
