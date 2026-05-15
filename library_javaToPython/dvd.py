from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def __str__(self):
        return super().__str__() + "\nDuration: " + str(self.__duration) + " minutes"
