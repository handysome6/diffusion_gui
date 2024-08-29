from PySide6.QtCore import QRunnable, QThread, QObject, Signal


class Signal(QObject):
    finished = Signal()


class RobotRunThread(QRunnable):
    def __init__(self, robot, script_path):
        super().__init__()
        self.robot = robot
        self.script_path = script_path
        self.signals = Signal()
        self.is_running = True

    def print_program_state(self):
        pstate = self.robot.GetProgramState()    #查询程序运行状态,1-程序停止或无程序运行，2-程序运行中，3-程序暂停
        name = self.robot.GetLoadedProgram()     #查询已加载的作业程序名
        print("the robot program state is:",pstate[1])
        print("the robot program name is:",name[1])
        QThread.msleep(1000)

    def run(self):
        ret = self.robot.RobotEnable(1)   #This function is enabled on the robot. After the robot is powered on, it is automatically enabled by default
        print("Enable the robot", ret)

        #机器人webapp程序使用接口
        self.robot.Mode(0)   #机器人切入自动运行模式
        self.print_program_state()
        ret = self.robot.ProgramLoad(self.script_path)   #加载要执行的机器人程序, lua程序需要先在webapp上编写好
        print("加载要执行的机器人程序错误码", ret)
        ret = self.robot.ProgramRun()
        print("Run lua error code:", ret)

        QThread.msleep(1000)

        # WAIT FOR ROBOT TO finish
        while self.is_running:
            _, pstate = self.robot.GetProgramState()    #查询程序运行状态,1-程序停止或无程序运行，2-程序运行中，3-程序暂停
            # print(pstate)
            if pstate == 1:
                ret = self.signals.finished.emit()
                return
            else:
                QThread.msleep(1000)

        
    def close(self):
        self.is_running = False
        self.robot.ProgramStop()


