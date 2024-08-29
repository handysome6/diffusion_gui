from pathlib import Path
from loguru import logger
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThreadPool, QProcess
from PySide6.QtGui import QCloseEvent

from diffusion_gui.fairino import Robot
from .robot_thread import RobotRunThread
from .ui_forms.gui_ui import Ui_Form


class DiffusionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit_scriptpath.setText('/fruser/simutrack.lua')

        self.ui.pushButton_runscript.clicked.connect(self.run_lua_script)
        self.ui.pushButton_startrtab.clicked.connect(self.start_rtabmap)
        self.ui.pushButton_stoprtab.clicked.connect(self.stop_rtabmap)
        self.ui.pushButton_convertrtab.clicked.connect(self.convert_rtabmap)

        # 与机器人控制器建立连接，连接成功返回一个机器人对象
        self.robot = Robot.RPC('192.168.58.2')

    def run_lua_script(self):
        script_path = self.ui.lineEdit_scriptpath.text()
        self.script_path = script_path
        self.ui.message_broswer.append("\n====================Lua Scirpt starting====================\n")

        self.robot_thread = RobotRunThread(self.robot, self.script_path)
        self.robot_thread.signals.finished.connect(self.on_thread_finished)
        QThreadPool.globalInstance().start(self.robot_thread)

        self.ui.pushButton_runscript.setEnabled(False)

    def on_thread_finished(self):
        self.ui.message_broswer.append("\n====================Lua Scirpt finished====================\n")
        self.ui.pushButton_runscript.setEnabled(True)

    def start_rtabmap(self):
        self.ui.message_broswer.append("\n====================RTABMAP starting====================\n")
        self.rtab_process = QProcess()
        # self.rtab_process.readyReadStandardOutput.connect(self.on_rtab_output)
        self.rtab_process.readyReadStandardError.connect(self.on_rtab_error)
        self.rtab_process.finished.connect(self.on_rtab_finished)
        self.rtab_process.start("roslaunch", ['spacemouse_pkg', 'multi_cam.launch', "serial_no:=936322070979"]) # 936322070979 141322251540

    def on_rtab_error(self):
        data = self.rtab_process.readAllStandardError()
        self.ui.message_broswer.append(data.data().decode('utf8'))

    def on_rtab_finished(self):
        self.ui.message_broswer.append("\n====================RTABMAP finsihed====================\n")

    def stop_rtabmap(self):
        import os
        import signal
        pid = self.rtab_process.processId()
        logger.info(f"qprocess pid: {pid}")
        os.kill(pid, signal.SIGINT)

    def convert_rtabmap(self):
        self.ui.message_broswer.append("\n====================Convert PC starting====================\n")
        self.convert_process = QProcess()
        self.convert_process.readyReadStandardOutput.connect(self.on_rtab_output)
        self.convert_process.finished.connect(self.on_convert_finished)

        saving_path = Path("data")
        saving_path.mkdir(parents=True, exist_ok=True)
        idx = len(list(saving_path.iterdir()))
        self.convert_process.start("rtabmap-export", ["--output", f"{idx}", "--output_dir", f"{saving_path}", '/home/hkcrc/.ros/rtabmap.db'])

    def on_rtab_output(self):
        data = self.convert_process.readAllStandardOutput()
        self.ui.message_broswer.append(data.data().decode('utf8'))

    def on_convert_finished(self):
        self.ui.message_broswer.append("\n====================Convert PC finsihed====================\n")

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.robot_thread is not None:
            self.robot_thread.close()
        return super().closeEvent(event)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    widget = DiffusionGUI()
    widget.show()

    sys.exit(app.exec_())
