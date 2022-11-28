class Example:
    example_field = 10

    def __init__(self):
        self.__example_field = 10

    def get_example_field(self):
        return self.__example_field

    def set_example_field(self, value_field):
        if value_field < 0:
            self.__example_field = 0
        else:
            self.__example_field = value_field

    example_field = property(get_example_field, set_example_field)