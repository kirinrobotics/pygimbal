import time
from pygimbal import control
from threading import Thread

master_gimbal = control.init_mav_connector('/dev/ttyUSB0', 1, 154, 115200)
system = master_gimbal.source_system
component = master_gimbal.source_component

maintain_connection_threading = Thread(target=control.maintain_connection, args=[master_gimbal], daemon=True)
maintain_connection_threading.start()

orientation_theading = Thread(target=control.get_orientation, args=[master_gimbal], daemon=True)
orientation_theading.start()

while True:
    try:
        control.control_gimbal(master_gimbal, system, component, tilt=45, roll=0, pan=45)
        time.sleep(2)
        control.control_gimbal(master_gimbal, system, component, tilt=0, roll=0, pan=0)
        time.sleep(2)
        control.control_gimbal(master_gimbal, system, component, tilt=45, roll=0, pan=-45)
        time.sleep(2)
        control.control_gimbal(master_gimbal, system, component, tilt=0, roll=0, pan=0)
        time.sleep(2)
    except KeyboardInterrupt:
        break