if __name__ == "__main__":
    from context import diffusion_gui
    from diffusion_gui.fairino import Robot
    import time
    from icecream import ic

    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    def print_program_state():
        ret, pstate = robot.GetProgramState()    #查询程序运行状态,1-程序停止或无程序运行，2-程序运行中，3-程序暂停
        linenum = robot.GetCurrentLine()    #查询当前作业程序执行的行号
        name = robot.GetLoadedProgram()     #查询已加载的作业程序名
        print(type(pstate))
        print("the robot program state is:", pstate)
        time.sleep(1)

    #机器人webapp程序使用接口
    robot.Mode(0)   #机器人切入自动运行模式
    print_program_state()
    ret = robot.ProgramLoad('/fruser/simutrack.lua')   #加载要执行的机器人程序，testPTP.lua程序需要先在webapp上编写好
    print("加载要执行的机器人程序错误码", ret)
    ret = robot.ProgramRun()     #执行机器人程序
    print("执行机器人程序错误码", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramPause()   #暂停正在执行的机器人程序
    print("暂停正在执行的机器人程序错误码", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramResume()  #恢复暂停执行的机器人程序
    print("恢复暂停执行的机器人程序错误码", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramStop()    #停止正在执行的机器人程序
    print("停止正在执行的机器人程序", ret)
    time.sleep(2)
    print_program_state()