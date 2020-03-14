class BeautyBean(object):
    def to_string(self):
        print(self.parent_name + "  " + self.name + "  " + self.thumbnail)

    def __init__(self, parent_name, name, thumbnail, img, beauty_list):
        self.parent_name = parent_name
        self.name = name
        self.thumbnail = thumbnail
        self.img = img
        self.beauty_list = beauty_list
