"""
    pip install obsws-python
    用法备注： .imagedata -> .image_data 每个命令的词之间加 _(下划线)，且字母都为小写
"""
import base64
import obsws_python as obs
import json


def strToImage(img, filename):
    image_str = img[22:]  # 截掉图片无效部分"data:image/jpg;base64,"
    image_str = image_str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)  # 将图片存到当前文件的fileimage文件中
    image_json.close()


if __name__ == '__main__':
    # pass conn info if not in config.toml
    cl = obs.ReqClient(host='localhost', port=4455, password='D9AQaWOH0b8Tu0Xn', timeout=3)
    # GetVersion, returns a response object
    resp = cl.get_version()
    # Access it's field as an attribute
    print(f"OBS Version: {resp.obs_version}")

    # SetCurrentProgramScene
    # cl.set_current_program_scene("终点")  # 切换终点场景

    # 查询返回json数据
    # resp = cl.send("GetVersion", raw=True)
    # print(f"response data: {resp}")
    # resp = cl.create_scene('第一视图')
    # resp = cl.remove_scene('第一视图')
    # resp = cl.get_source_screenshot('终点', "jpg", None, None, 100)
    # print(resp.image_data)
    # strToImage(resp.image_data, './a.jpg')
    resp = cl.get_scene_item_list('现场')
    print(resp.scene_items[0])
    for item in resp.scene_items:
        print(item['sourceName'])

    cl.set_scene_item_enabled('现场', 8, True)  # 打开视频来源
