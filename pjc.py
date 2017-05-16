import time

import pyvjoy


j = pyvjoy.VJoyDevice(1)

def reset():
    j.data.wAxisX = 0x4000
    j.data.wAxisXRot = 0x4000
    j.data.wAxisY = 0x4000
    j.data.wAxisYRot = 0x4000
    j.data.wAxisZ = 0x0000
    j.data.wAxisZRot = 0x0000
    j.update()


def toggle_button(button, delay=0.05, press_time=0.25, repeat=1):
    time.sleep(delay)
    for event in range(repeat):
        j.set_button(button, 1)
        time.sleep(press_time)
        j.set_button(button, 0)


def set_view():
    pass

if __name__ == '__main__':
    pass

