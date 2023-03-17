<img src="./docs/imgs/pygimbal.png" width="100%">

# pygimbal

`Pygimbal` is an open source software developed in `Python`, designed for controlling gimbals using the `Mavlink protocol`. It allows users to control the gimbal's tilt, pan, and roll angles, as well as retrieve real-time angle values.

## Install

```
pip install pygimbal
```

## Getting Started

How to control gimbal via Mavlink with Python:

> Note: you need to give permission to gimbal uart port first.

```shell
sudo chmod a+wrx /dev/ttyUSB0
```

Sample code:


```python
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
```

Output:

```
[ACTION]: Mavlink is connecting to /dev/ttyUSB0
[MESSAGE]: Successful Connection to /dev/ttyUSB0 1 154
[Control] Gimbal Pitch - Yaw 45 45
[ORIENTATION] Til, Pan, Roll:  0.1949998289346695 0.02197265625 0.023102451115846634
[ORIENTATION] Til, Pan, Roll:  0.19493775069713593 0.02197265625 0.02414652332663536
[ORIENTATION] Til, Pan, Roll:  0.19543787837028503 0.02197265625 0.02471373975276947
[ORIENTATION] Til, Pan, Roll:  0.19867371022701263 0.02197265625 0.0238236952573061
```

Result:

<div align='center'>
  <img src="./docs/imgs/result.gif" width="70%">
</div>

## Author

```
github: winter2897
mail: haiquantran2897@gmail.com
```

## Licence

Pygimbal is made available under the permissive open source Apache 2.0 License.

Copyright 2023 Kirins Robotics, Inc.