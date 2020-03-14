class CategoryBean(object):
    def to_string(self):
        print(self.c_name + "  " + self.c_child_list[0])

    def __init__(self, c_name, c_child_list):
        self.c_name = c_name
        self.c_child_list = c_child_list
