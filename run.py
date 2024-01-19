from pynput import mouse, keyboard
from pynput.keyboard import Listener, Key
import time
import json

with open('operation.json', 'r') as f:
    operation = json.load(f)

SLEEPTIME = 1 # 每次操作的间隔时间
REFRESH_SLEEP = 30 # 刷新网页的等待时间
ITERATION = 50 # 重复次数
mouse = mouse.Controller()
keyboard = keyboard.Controller()
scroll = 0
iter = 0

time.sleep(5) # 五秒后程序开始

# 定义一个全局变量来控制循环
continue_loop = True


# 定义一个监听器来监听键盘事件
def on_press(key):
    global continue_loop
    # 检查是否按下了F10键
    if key == Key.f10:
        continue_loop = False

# 开始监听键盘事件


with Listener(on_press=on_press) as listener:
    while continue_loop:
        # 复现鼠标操作
        with keyboard.pressed(Key.ctrl):
            keyboard.press('r')
            keyboard.release('r')
            time.sleep(REFRESH_SLEEP)
        for action in operation:
            if action["action"] == "left_click":
                if scroll != 0:
                    mouse.scroll(0, scroll)
                    scroll = 0
                    time.sleep(SLEEPTIME)
                mouse.position = action["position"]
                mousePosition = mouse.position
                mouse.press(mouse.Button.left)
                mouse.release(mouse.Button.left)
                time.sleep(SLEEPTIME)
            elif action["action"] == "scroll_down":
                scroll -= 1
                mouse.position = action["position"]
                mousePosition = mouse.position
            elif action["action"] == "scroll_up":
                scroll += 1
                mouse.position = action["position"]
                mousePosition = mouse.position

        iter += 1
        if iter == ITERATION:
            break
