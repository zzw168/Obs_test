"""
    https://github.com/obsproject/obs-websocket/
    pip install obsws-python
    用法备注： .imagedata -> .image_data 每个命令的词之间加 _(下划线)，且字母都为小写
    https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
"""
import sys

import obsws_python as obs
import json
from PyQt5.QtWidgets import QApplication, QMainWindow

from Obs_test_Ui import Ui_MainWindow
from tools_unit import *


class MyUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super(MyUi, self).setupUi(MainWindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = MyUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    cl_requst = obs.ReqClient()
    cl_event = obs.EventClient()

    # GetVersion, returns a response object
    resp = cl_requst.get_version()
    # Access it's field as an attribute
    print(f"OBS Version: {resp.obs_version}")
    # 注册事件
    # cl_event.callback.register(on_scene_created)
    # 视图变化事件
    cl_event.callback.register(on_current_program_scene_changed)    # 场景变化
    cl_event.callback.register(on_scene_item_enable_state_changed)  # 来源变化

    cl_event.callback.register(on_record_state_changed)  # 录制状态
    cl_event.callback.register(on_stream_state_changed)  # 直播流状态
    cl_event.callback.register(on_get_stream_status)  # 直播流状态

    # SetCurrentProgramScene
    # cl.set_current_program_scene("终点")  # 切换终点场景

    # # 查询返回json数据
    # resp = cl.send("GetVersion", raw=True)
    # print(f"response data: {resp}")
    # # 创建视图，删除视图
    # resp = cl.create_scene('第一视图')
    # resp = cl.remove_scene('第一视图')
    # # 截取场景照片并保存
    # resp = cl.get_source_screenshot('终点', "jpg", None, None, 100)
    # str2image(resp.image_data, './a.jpg')
    # 提取场景内所有来源的列表
    # resp = cl.get_scene_item_list('现场')
    # print(resp.scene_items[0])
    # for item in resp.scene_items:
    #     print(item['sourceName'])
    # # 打开,关闭来源
    # cl_requst.set_scene_item_enabled('现场', 8, True)  # 打开视频来源

    sys.exit(app.exec_())
