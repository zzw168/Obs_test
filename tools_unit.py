import base64


def strToImage(img, filename):
    image_str = img[22:]  # 截掉图片无效部分"data:image/jpg;base64,"
    image_str = image_str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)  # 将图片存到当前文件的fileimage文件中
    image_json.close()


"""
    OBS callback 回调函数
"""


def on_scene_created(data):
    print(data.scene_uuid)
    print(data.scene_name)
    print(data.is_group)


def on_current_program_scene_changed(data):
    print(data.scene_uuid)
    print(data.scene_name)


"""
    OBS callback 回调函数 结束
"""
