from pynput import mouse, keyboard
import time
import json

# 记录鼠标操作
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            operation.append({"action": "left_click", "position": (x, y)})
            print(f"Left Click at {x}, {y}")
    elif button == mouse.Button.right:
        if not pressed:  # 检查右键是否被释放
            pass

def on_scroll(x, y, dx, dy):
    if dy > 0:
        operation.append({"action": "scroll_up", "position": (x, y), "units": 1})
        print(f"Scroll Up at {x}, {y}")
    elif dy < 0:
        operation.append({"action": "scroll_down", "position": (x, y), "units": -1})
        print(f"Scroll Down at {x}, {y}")

    # 初始化操作列表


operation = []


def on_key_release(key):
    # 按下f11开始记录
    if key == keyboard.Key.f11:
        mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
        mouse_listener.start()
        print('开始记录')
    if key == keyboard.Key.f10:
        print('停止记录')
        return False


# 开始监听鼠标操作，记录操作到列表中
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

with open('operation.json', 'w') as f:
    json.dump(operation, f)