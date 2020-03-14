# 响应
class Response(object):
    def __init__(self, code, content):
        self.code = code
        self.content = content


# 返回内容
class Content(object):
    def __init__(self, fun_code, category_list):
        self.fun_code = fun_code
        self.category_list = category_list


# 分类
class Category(object):
    def __init__(self, name, album_list):
        self.name = name
        self.album_list = album_list


# 专辑
class Album(object):
    def __init__(self, album_name, thumbnail, image_list):
        self.album_name = album_name
        self.thumbnail = thumbnail
        self.image_list = image_list
