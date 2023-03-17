#!/bin/bash
# author='winter2897'

import os
os.environ['MAVLINK20'] = '1'
os.environ['MAVLINK_DIALECT'] = 'ardupilotmega'

import time
from threading import Thread
from pymavlink import mavutil

def init_mav_connector(device, source_system, source_component, baud=115200):

    print('[ACTION]: Mavlink is connecting to', device)
    master = mavutil.mavlink_connection(device, baud, source_system, source_component, autoreconnect=True)
    master.mav.heartbeat_send(2,0,0,0,0,3)
    master.wait_heartbeat()
    print('[MESSAGE]: Successful Connection to', device, master.source_system, master.source_component)

    return master

def control_gimbal(master,target, source, tilt, roll, pan):

    master.mav.command_long_send(
            target,
            source,
            mavutil.mavlink.MAV_CMD_DO_MOUNT_CONTROL, 
            1,
            tilt,
            roll,
            pan,
            0, 0, 0,
            mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING)
    
    print('[Control] Gimbal Pitch - Yaw', tilt, pan)
            
def maintain_connection(master):
    while True:
        master.mav.heartbeat_send(2,0,0,0,0,3)
        time.sleep(0.5)

def get_orientation(master):

    while True:
        msg = master.recv_match()
        if msg:
            if msg.get_type() == 'MOUNT_ORIENTATION':
                tilt = msg.pitch
                pan = msg.yaw
                roll = msg.roll
                print('[ORIENTATION] Til, Pan, Roll: ', tilt, pan, roll)
        time.sleep(0.01)

if __name__=="__main__":

    master_gimbal = init_mav_connector('/dev/ttyUSB0', 1, 154, 115200)
    system = master_gimbal.source_system
    component = master_gimbal.source_component

    maintain_connection_threading = Thread(target=maintain_connection, args=[master_gimbal], daemon=True)
    maintain_connection_threading.start()

    orientation_theading = Thread(target=get_orientation, args=[master_gimbal], daemon=True)
    orientation_theading.start()

    while True:
        control_gimbal(master_gimbal, system, component, tilt=45, roll=0, pan=45)
        time.sleep(2)
        control_gimbal(master_gimbal, system, component, tilt=0, roll=0, pan=0)
        time.sleep(2)
        control_gimbal(master_gimbal, system, component, tilt=45, roll=0, pan=-45)
        time.sleep(2)
        control_gimbal(master_gimbal, system, component, tilt=0, roll=0, pan=0)
        time.sleep(2)

