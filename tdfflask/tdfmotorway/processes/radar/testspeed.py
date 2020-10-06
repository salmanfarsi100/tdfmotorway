from SpeedMonitorV1_1 import SpeedMonitor
import time

confpath="config.ini"

Sp=SpeedMonitor(confpath)
time.sleep(10)
Sp.stopserial()
