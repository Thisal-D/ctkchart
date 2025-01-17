[![Language](https://img.shields.io/badge/Language-English-blue)](README.md)

<div align="center">

[![ctkchart](https://snyk.io/advisor/python/ctkchart/badge.svg)](https://snyk.io/advisor/python/ctkchart)

# ctkchart

[![PyPI version](https://badge.fury.io/py/ctkchart.svg)](https://pypi.org/project/ctkchart/)

[![Downloads](https://static.pepy.tech/badge/ctkchart)](https://pepy.tech/project/ctkchart) ![Downloads last 6 month](https://static.pepy.tech/personalized-badge/ctkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month) [![Downloads](https://static.pepy.tech/badge/ctkchart/month)](https://pepy.tech/project/ctkchart) [![Downloads](https://static.pepy.tech/badge/ctkchart/week)](https://pepy.tech/project/ctkchart)


![PyPI - License](https://img.shields.io/badge/license-MIT-blue)
![LOC](https://tokei.rs/b1/github/Thisal-D/ctkchart?category=lines)

</div>

**<li>ctkchart 是一个用于在 customtkinter 中创建实时更新折线图的 Python 库。</li>**

---

### 特性

- **实时更新**: 显示带有实时数据的折线图。
- **多条线**: 支持在同一图表上绘制多条线，便于比较。
- **颜色定制**: 自定义颜色以匹配您的应用程序设计或数据表示。
- **动态颜色变化**: 实现暗模式和亮模式下的动态颜色变化。
- **字体定制**: 调整文本元素的字体以增强可读性。
- **尺寸定制**: 根据不同显示尺寸和布局自定义图表尺寸。

[**查看最新更新 | 更改**](CHANGES_zh.md)

---

### 导入与安装
* **安装**
    ```
    pip install ctkchart
    ```

* **导入**
    ``` python
    import ctkchart
    ```

---

### 简单示例
- **导入库**
    ``` python
    import tkchart
    ```
    
- **创建折线图并放置图表**
    ``` python
    chart = ctkchart.CTkLineChart(
        master=root,
        x_axis_values=("a", "b", "c", "d", "e", "f"),
        y_axis_values=(100, 900)
    )
    chart.place(x=10, y=10)
    ```

- **创建折线**
    ``` python
    line = ctkchart.CTkLine(master=chart)
    ```

- **显示数据**
    使用循环显示数据
    ``` python
    def loop():
        while True:
            random_data = random.choice(range(100, 900))
            chart.show_data(line=line, data=[random_data])
            time.sleep(1)
    
    #调用线程
    theading.Thread(target=loop).start()
    ```
    
---

### 链接

- **文档 :** [文档](documentation)
    - [英文文档](documentation/DOCUMENTATION_en.md)
    - [中文文档](documentation/DOCUMENTATION_zh.md)
- **Python 官方 :** [ctkchart](https://pypi.org/project/ctkchart/)

---

### 您可以完成的任务

- **简单示例**

    https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9
    
    ``` python
    import customtkinter as ctk  # 导入 customtkinter 库作为 ctk
    import ctkchart  # 导入 ctkchart 模块用于创建图表
    import random  # 导入 random 模块用于生成随机数据
    import threading  # 导入 threading 模块用于并发执行任务
    import time  # 导入 time 模块用于添加延时

    # 创建根窗口并配置
    root = ctk.CTk()
    root.configure(fg_color="#0d1117")
    root.geometry("720x430+200+200")  

    # 创建折线图控件
    line_chart = ctkchart.CTkLineChart(
        master=root,  # 设置根窗口为父容器
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴值
        y_axis_values=(0, 1000)  # Y轴值（范围）
    )

    line_chart.pack(pady=15)  # 将折线图控件放入根窗口

    # 创建折线
    line = ctkchart.CTkLine(master=line_chart)  # 设置折线图为父容器

    def display_data():
        """函数用于持续在折线图上显示随机数据。"""
        while True:
            random_data = [random.choice(range(0, 1000))]  # 生成 0 到 1000 之间的随机数据
            line_chart.show_data(line=line, data=random_data)  # 在折线图上显示随机数据
            time.sleep(0.5)  # 在下一次迭代之前暂停 0.5 秒

    # 在新线程中调用 display_data 函数
    threading.Thread(target=display_data).start()

    # 启动主事件循环
    root.mainloop()
    ```
    ---

- **简单风格**

    https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e

    ``` python
    import customtkinter as ctk  # 导入 customtkinter 库作为 ctk
    import ctkchart  # 导入 ctkchart 模块用于创建图表
    import random  # 导入 random 模块用于生成随机数据
    import threading  # 导入 threading 模块用于并发执行任务
    import time  # 导入 time 模块用于添加延时

    # 创建根窗口并配置
    root = ctk.CTk()
    root.configure(fg_color="#0d1117")
    root.geometry("720x430+200+200")  

    # 创建折线图控件
    line_chart = ctkchart.CTkLineChart(
        master=root,  # 设置根窗口为父容器
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴值
        y_axis_values=(0, 1000),  # Y轴值（范围）
        y_axis_label_count=10, # 设置Y轴标签数量为10
    )

    line_chart.pack(pady=15)  # 将折线图控件放入根窗口

    # 创建折线
    line = ctkchart.CTkLine(
        master=line_chart,  # 设置折线图为父容器
        size=2,  # 设置折线宽度为 2
        fill="enabled" # 启用填充效果
    )  

    def display_data():
        """函数用于持续在折线图上显示随机数据。"""
        while True:
            random_data = [random.choice(range(0, 1000))]  # 生成 0 到 1000 之间的随机数据
            line_chart.show_data(line=line, data=random_data)  # 在折线图上显示随机数据
            time.sleep(0.5)  # 在下一次迭代之前暂停 0.5 秒

    # 在新线程中调用 display_data 函数
    threading.Thread(target=display_data).start()

    # 启动主事件循环
    root.mainloop()
    ```
    ---

- **两条线，不同的线型**

    https://github.com/Thisal-D/ctkchart/assets/93121062/9bc35a39-a8ca-4942-9fc7-a1c89d1bd1bc

    ```python
    import customtkinter as ctk  # 导入 customtkinter 库作为 ctk
    import ctkchart  # 导入 ctkchart 模块用于创建图表
    import random  # 导入 random 模块用于生成随机数据
    import threading  # 导入 threading 模块用于并发运行任务
    import time  # 导入 time 模块用于添加延迟

    # 创建根窗口并配置
    root = ctk.CTk()
    root.configure(fg_color=("#ffffff", "#0d1117"))
    root.geometry("720x430+200+200")  

    # 创建线性图表小部件
    line_chart = ctkchart.CTkLineChart(
        master=root,  # 设置根窗口为主窗口
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴的值
        y_axis_values=(0, 1000),  # Y轴的值（范围）
        y_axis_label_count=10, # 设置Y轴标签数量为10
    )

    line_chart.pack(pady=15)  # 将线图部件打包到根窗口中

    line1 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        color=("#5dffb6", "#5dffb6"),  # 轻主题为#5dffb6，暗主题为#5dffb6
        size=2,  # 设置线的大小为2
        style="dashed",  # 将线的样式更改为虚线
        style_type=(10, 5),  # 设置虚线的宽度和虚线之间的间隔
    )

    line2 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        color=("#FFBAD2", "#FFBAD2"),  # 轻主题为#FFBAD2，暗主题为#FFBAD2
        size=2,  # 设置线的大小为2
        point_highlight="enabled",  # 启用点高亮
        point_highlight_color=("#FFBAD2", "#FFBAD2"),  # 设置高亮颜色
    )

    def display_data():
        """函数：持续在图表上显示随机数据。"""
        while True:
            random_data = [random.choice(range(0, 1000))]  # 生成 0 到 1000 之间的随机数据
            line_chart.show_data(line=line1, data=random_data)  # 显示数据在 line1 上
            random_data = [random.choice(range(0, 1000))]  # 生成新的随机数据
            line_chart.show_data(line=line2, data=random_data)  # 显示数据在 line2 上
            time.sleep(0.5)  # 暂停 0.5 秒钟再进行下一次迭代

    # 以独立线程运行 display_data 函数
    threading.Thread(target=display_data).start()

    # 启动主事件循环
    root.mainloop()
    ```

--- 

- **三条线，不同的线型**

    https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134

    ```python
    import customtkinter as ctk  # 导入 customtkinter 库作为 ctk
    import ctkchart  # 导入 ctkchart 模块用于创建图表
    import random  # 导入 random 模块用于生成随机数据
    import threading  # 导入 threading 模块用于并发运行任务
    import time  # 导入 time 模块用于添加延迟

    # 创建根窗口并配置
    root = ctk.CTk()
    root.configure(fg_color=("#ffffff", "#0d1117"))
    root.geometry("720x430+200+200")  

    # 创建线性图表小部件
    line_chart = ctkchart.CTkLineChart(
        master=root,  # 设置根窗口为主窗口
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴的值
        y_axis_values=(0, 1000),  # Y轴的值（范围）
        y_axis_label_count=10, # 设置Y轴标签数量为10
    )

    line_chart.pack(pady=15)  # 将线图部件打包到根窗口中

    # 创建线1
    line1 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        size=2,  # 设置线的大小为2
        fill="enabled"  # 启用线填充
    )

    line2 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        color=("#5dffb6", "#5dffb6"),  # 轻主题为#5dffb6，暗主题为#5dffb6
        size=2,  # 设置线的大小为2
        style="dashed",  # 将线的样式更改为虚线
        style_type=(10, 5),  # 设置虚线的宽度和虚线之间的间隔
    )

    line3 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        color=("#FFBAD2", "#FFBAD2"),  # 轻主题为#FFBAD2，暗主题为#FFBAD2
        size=2,  # 设置线的大小为2
        point_highlight="enabled",  # 启用点高亮
        point_highlight_color=("#FFBAD2", "#FFBAD2"),  # 设置高亮颜色
    )

    def display_data():
        """函数：持续在图表上显示随机数据。"""
        while True:
            random_data = [random.choice(range(0, 1000))]  # 生成 0 到 1000 之间的随机数据
            line_chart.show_data(line=line1, data=random_data)  # 显示数据在 line1 上
            random_data = [random.choice(range(0, 1000))]  # 生成新的随机数据
            line_chart.show_data(line=line2, data=random_data)  # 显示数据在 line2 上
            random_data = [random.choice(range(0, 1000))]  # 生成新的随机数据
            line_chart.show_data(line=line3, data=random_data)  # 显示数据在 line3 上
            time.sleep(0.5)  # 暂停 0.5 秒钟再进行下一次迭代

    # 以独立线程运行 display_data 函数
    threading.Thread(target=display_data).start()

    # 启动主事件循环
    root.mainloop()
    ```

---

- **进阶**（实际上只是添加了两个属性）

    https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d

    ```python
    import customtkinter as ctk  # 导入 customtkinter 库作为 ctk
    import ctkchart  # 导入 ctkchart 模块用于创建图表
    import random  # 导入 random 模块用于生成随机数据
    import threading  # 导入 threading 模块用于并发运行任务
    import time  # 导入 time 模块用于添加延迟

    # 创建根窗口并配置
    root = ctk.CTk()
    root.configure(fg_color=("#ffffff", "#0d1117"))
    root.geometry("720x430+200+200")  

    # 创建线性图表小部件
    line_chart = ctkchart.CTkLineChart(
        master=root,  # 设置根窗口为主窗口
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X轴的值
        y_axis_values=(0, 1000),  # Y轴的值（范围）
        y_axis_label_count=10, # 设置Y轴标签数量为1
        y_axis_section_count=10,
        x_axis_section_count=10,
    )

    line_chart.pack(pady=15)  # 将线图部件打包到根窗口中

    line1 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        color=("#5dffb6", "#5dffb6"),  # 轻主题为#5dffb6，暗主题为#5dffb6
        size=2,  # 设置线的大小为2
        style="dashed",  # 将线的样式更改为虚线
        style_type=(10, 5),  # 设置虚线的宽度和虚线之间的间隔
    )

    line2 = ctkchart.CTkLine(
        master=line_chart,  # 设置线图的主窗口
        color=("#FFBAD2", "#FFBAD2"),  # 轻主题为#FFBAD2，暗主题为#FFBAD2
        size=2,  # 设置线的大小为2
        point_highlight="enabled",  # 启用点高亮
        point_highlight_color=("#FFBAD2", "#FFBAD2"),  # 设置高亮颜色
    )

    def display_data():
        """函数：持续在图表上显示随机数据。"""
        while True:
            random_data = [random.choice(range(0, 1000))]  # 生成 0 到 1000 之间的随机数据
            line_chart.show_data(line=line1, data=random_data)  # 显示数据在 line1 上
            random_data = [random.choice(range(0, 1000))]  # 生成新的随机数据
            line_chart.show_data(line=line2, data=random_data)  # 显示数据在 line2 上
            time.sleep(0.5)  # 暂停 0.5 秒钟再进行下一次迭代

    # 以独立线程运行 display_data 函数
    threading.Thread(target=display_data).start()

    # 启动主事件循环
    root.mainloop()
    ```

---

-  #### 轻主题和暗主题

    **对于 ctkchart 中涉及颜色的每个参数，您可以提供以下任意一种**： 
    - 一个字符串表示颜色。 
    - 一个包含两个字符串的元组，第一个字符串表示轻主题颜色，第二个字符串表示暗主题颜色。
    
    https://github.com/user-attachments/assets/9fed4b83-5b03-4ea0-82a0-36029dfc93dd

---

**探索可自定义的功能，如颜色、字体等，详细内容请参考文档。**

#### 请参考完整文档
- [**英文文档**](documentation/DOCUMENTATION_en.md)
- [**中文文档**](documentation/DOCUMENTATION_zh.md)

---

#### 贡献者
- [<img src="https://github.com/childeyouyu.png?size=25" width="25">](https://github.com/childeyouyu) [youyu](https://github.com/childeyouyu)
