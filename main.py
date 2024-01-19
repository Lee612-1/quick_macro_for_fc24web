import tkinter as tk
import tkinter.font as font
import subprocess


def run_script1():
    subprocess.run(["python", "record.py"])


def run_script2():
    subprocess.run(["python", "run.py"])


def open_subwindow1(parent):
    # 创建子窗口
    subwindow = tk.Toplevel(parent)
    subwindow.title("记录")
    subwindow.geometry("300x100+50+200")

    # 在子窗口上添加内容
    sub_label1 = tk.Label(subwindow, text="按f11开始记录")
    sub_label2 = tk.Label(subwindow, text="按f10停止记录")
    sub_button = tk.Button(subwindow, text="完成", command=lambda: subwindow.destroy())
    sub_label1.place(x=100, y=10)
    sub_label2.place(x=100, y=30)
    sub_button.place(x=125, y=60)

def open_subwindow2(parent):
    # 创建子窗口
    subwindow = tk.Toplevel(parent)
    subwindow.title("运行")
    subwindow.geometry("300x100+50+200")

    # 在子窗口上添加内容
    sub_label1 = tk.Label(subwindow, text="5秒内开始运行")
    sub_label2 = tk.Label(subwindow, text="按f10停止运行")
    sub_button = tk.Button(subwindow, text="完成", command=lambda: subwindow.destroy())
    sub_label1.place(x=100, y=10)
    sub_label2.place(x=100, y=30)
    sub_button.place(x=125, y=60)

root = tk.Tk()
root.title("按键小精灵")
root.geometry("300x100+50+200")

font_1 = font.Font(family='Helvetica', size=10, weight='bold')
button1 = tk.Button(root, text="记录", bg="Red", foreground="White", font= font_1, command=lambda: [run_script1, open_subwindow1(root)])
button2 = tk.Button(root, text="运行", bg="Green", foreground="White", font= font_1, command=lambda: [run_script2, open_subwindow2(root)])
button1.place(x=75, y=25, width=50, height=50)
button2.place(x=175, y=25, width=50, height=50)

root.mainloop()