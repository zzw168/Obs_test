"""
    https://github.com/obsproject/obs-websocket/
    pip install obsws-python
    用法备注： .imagedata -> .image_data 每个命令的词之间加 _(下划线)，且字母都为小写
    https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
"""
import sys
import time

import obsws_python as obs
import json

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QTableWidgetItem

from Obs_test_Ui import Ui_MainWindow
from tools_unit import *

"""
    OBS callback 回调函数
    cl_event.callback.register(on_record_state_changed)  # 以这个形式调用，注册回调函数
"""


# 场景新建事件
def on_scene_created(data):
    print(data.scene_uuid)
    print(data.scene_name)
    print(data.is_group)


# 场景切换事件
def on_current_program_scene_changed(data):
    print("程序场景变化")
    print(data.scene_uuid)
    print(data.scene_name)

    get_source_list(data.scene_name)


# 场景预览改变事件
def on_current_preview_scene_changed(data):
    print("预览场景变化")
    print(data.scene_uuid)
    print(data.scene_name)


# 来源变化事件
def on_scene_item_enable_state_changed(data):
    print("来源元素变化")
    print(data.scene_uuid)
    print(data.scene_name)
    print(data.scene_item_id)
    print(data.scene_item_enabled)


# 流状态改变事件
def on_record_state_changed(data):
    print("录制状态变化")
    print(data.output_active)
    print(data.output_state)
    print(data.output_path)


# 流状态改变事件
def on_stream_state_changed(data):
    print("流状态变化")
    print(data.output_active)
    print(data.output_state)


# 来源变化事件
def on_get_stream_status(data):
    print("直播流状态")
    print(data.output_active)
    print(data.output_reconnecting)
    print(data.output_timecode)
    print(data.output_duration)
    print(data.output_congestion)
    print(data.output_bytes)
    print(data.output_skipped_frames)
    print(data.output_total_frames)


"""
    OBS callback 回调函数 结束
"""


class MyUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super(MyUi, self).setupUi(MainWindow)

        tb_sources = self.tableWidget_Sources
        tb_sources.horizontalHeader().resizeSection(0, 10)
        tb_sources.horizontalHeader().resizeSection(1, 160)
        # tb_sources.horizontalHeader().resizeSection(2, 30)
        tb_sources.setColumnHidden(2, True)
        tb_sources.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(245,245,245);}")
        tb_sources.verticalHeader().setStyleSheet("QHeaderView::section{background:rgb(245,245,245);}")


class SourceThead(QThread):
    _signal = pyqtSignal(object)

    def __init__(self):
        super(SourceThead, self).__init__()
        self.run_flg = ''

    def run(self) -> None:
        global source_list
        self._signal.emit('写表')


def source_signal_accept(msg):
    print(msg)
    source2table()


# 截取OBS图片
def get_picture():
    scence_current = ui.comboBox_Scenes.currentText()
    resp = cl_requst.get_source_screenshot(scence_current, "jpg", None, None, 100)
    print(resp.image_data)
    img = str2image(resp.image_data)
    pixmap = QPixmap()
    pixmap.loadFromData(img)
    pixmap = pixmap.scaled(ui.label_picture.size(), Qt.AspectRatioMode.KeepAspectRatio,
                           Qt.TransformationMode.SmoothTransformation)
    lab_p = ui.label_picture
    lab_p.clear()
    lab_p.setPixmap(pixmap)


def get_scenes_list():  # 刷新所有列表
    res = cl_requst.get_scene_list()  # 获取场景列表
    print(res.scenes)
    print(len(res.scenes))
    cb_scenes = ui.comboBox_Scenes
    cb_scenes.clear()
    for i, item in enumerate(res.scenes):
        cb_scenes.addItem(item['sceneName'])
    res = cl_requst.get_current_program_scene()  # 获取激活的场景
    scene_name = res.scene_name
    cb_scenes.setCurrentText(scene_name)


def get_source_list(scene_name):
    global source_list
    res = cl_requst.get_scene_item_list(scene_name)
    source_list = []
    for item in res.scene_items:
        source_list.append([item['sceneItemEnabled'], item['sourceName'], item['sceneItemId']])
        print(item)
    Source_Thead.start()


# 数据进表
def source2table():
    global source_list
    tb_sources = ui.tableWidget_Sources
    tb_sources.setRowCount(len(source_list))
    for i in range(0, len(source_list)):
        cb = QCheckBox()
        cb.setStyleSheet('QCheckBox{margin:6px};')
        cb.clicked.connect(source_enable)
        tb_sources.setCellWidget(i, 0, cb)
        if source_list[i][0] == True:
            tb_sources.cellWidget(i, 0).setChecked(True)
        print(source_list[i][0])
        for j in range(1, len(source_list[i])):
            item = QTableWidgetItem(str(source_list[i][j]))
            item.setTextAlignment(Qt.AlignCenter)
            # item.setFlags(QtCore.Qt.ItemFlag(63))   # 单元格可编辑
            tb_sources.setItem(i, j, item)


def scenes_change():  # 变换场景
    scene_name = ui.comboBox_Scenes.currentText()
    cl_requst.set_current_program_scene(scene_name)


def source_enable():  # 开关来源
    tb_source = ui.tableWidget_Sources
    row_num = tb_source.currentRow()
    source_list[row_num][0] = not (source_list[row_num][0])
    source_enable = source_list[row_num][0]
    cb_scene = ui.comboBox_Scenes
    scene_name = cb_scene.currentText()
    item_id = source_list[row_num][2]
    print(source_list)
    # # 打开,关闭来源
    cl_requst.set_scene_item_enabled(scene_name, item_id, source_enable)  # 打开视频来源


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = MyUi()
    ui.setupUi(MainWindow)
    MainWindow.show()

    source_list = []

    cl_requst = obs.ReqClient()  # 请求
    cl_event = obs.EventClient()  # 监听

    cl_event.callback.register(on_current_program_scene_changed)  # 场景变化
    cl_event.callback.register(on_scene_item_enable_state_changed)  # 来源变化
    cl_event.callback.register(on_record_state_changed)  # 录制状态
    cl_event.callback.register(on_stream_state_changed)  # 直播流状态
    cl_event.callback.register(on_get_stream_status)  # 直播流状态

    Source_Thead = SourceThead()  # 实时监控摄像头位置
    Source_Thead._signal.connect(source_signal_accept)

    get_scenes_list()  # 获取所有场景

    get_source_list(ui.comboBox_Scenes.currentText())

    ui.pushButton_GetPicture.clicked.connect(get_picture)
    ui.pushButton_ObsConnect.clicked.connect(get_source_list)
    ui.comboBox_Scenes.currentTextChanged.connect(scenes_change)

    # GetVersion, returns a response object
    resp = cl_requst.get_version()
    # Access it's field as an attribute
    print(f"OBS Version: {resp.obs_version}")

    # # 打开,关闭来源
    # cl_requst.set_scene_item_enabled('现场', 8, True)  # 打开视频来源

    sys.exit(app.exec_())
