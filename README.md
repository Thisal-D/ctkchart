[![Chinese](https://img.shields.io/badge/Language-中文-red)](README_zh.md)

<div align="center">

[![ctkchart](https://snyk.io/advisor/python/ctkchart/badge.svg)](https://snyk.io/advisor/python/ctkchart)

# ctkchart

[![PyPI version](https://badge.fury.io/py/ctkchart.svg)](https://pypi.org/project/ctkchart/)

[![Downloads](https://static.pepy.tech/badge/ctkchart)](https://pepy.tech/project/ctkchart) ![Downloads last 6 month](https://static.pepy.tech/personalized-badge/ctkchart?period=total&units=international_system&left_color=grey&right_color=BLUE&left_text=downloads%20last%206%20month) [![Downloads](https://static.pepy.tech/badge/ctkchart/month)](https://pepy.tech/project/ctkchart) [![Downloads](https://static.pepy.tech/badge/ctkchart/week)](https://pepy.tech/project/ctkchart)


![PyPI - License](https://img.shields.io/badge/license-MIT-blue)
![LOC](https://tokei.rs/b1/github/Thisal-D/ctkchart?category=lines)

</div>


**<li>ctkchart is a Python library for creating live updating line charts in customtkinter.</li>**

---

### Features

- **Live Update**: Display live data with line charts.
- **Multiple Lines**: Support for plotting multiple lines on the same chart for easy comparison.
- **Color Customization**: Customize colors to match your application's design or data representation.
- **Dynamic Color Change**: Dynamic Color Change for Dark & Light.
- **Font Customization**: Adjust fonts for text elements to enhance readability.
- **Dimension Customization**: Customize chart dimensions to fit various display sizes and layouts.

[**Check out what's new | Changes**](CHANGES_en.md)

---

### Importing & Installation
* **Installation**
    ```
    pip install ctkchart
    ```

* **Importing**
    ``` python
    import ctkchart
    ```
---


### Simple Guide
- **import package**
    ``` python
    import tkchart
    ```
    
- **Create Line Chart and place the chart**
    ``` python
    chart = ctkchart.CTkLineChart(
        master=root,
        x_axis_values=("a", "b", "c", "d", "e", "f"),
        y_axis_values=(100, 900)
    )
    chart.place(x=10, y=10)
    ```

- **Create Line**
    ``` python
    line = ctkchart.CTkLine(master=chart)
    ```

- **Display Data**
    display data using a loop
    ``` python
    def loop():
        while True:
            random_data = random.choice(range(100, 900))
            chart.show_data(line=line, data=[random_data])
            time.sleep(1)
    
    #call the loop as thead
    theading.Thread(target=loop).start()
    ```
    
---

### Links

- **Documentation :** [Documents](documentation)
    - [English doc.](documentation/DOCUMENTATION_en.md)
    - [Chinese doc.](documentation/DOCUMENTATION_zh.md)
- **Python official :** [ctkchart](https://pypi.org/project/ctkchart/)

---

### What You Can Accomplish

- **Simple**

    https://github.com/Thisal-D/ctkchart/assets/93121062/6f1e844f-d51c-467a-a3dc-ee03fea78fc9
    
    ``` python
    import customtkinter as ctk  # Importing the customtkinter library as ctk
    import ctkchart  # Importing the ctkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = ctk.CTk()
    root.configure(fg_color="#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = ctkchart.CTkLineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000)  # Y-axis values (range)
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    # Create a line for the line chart
    line = ctkchart.CTkLine(master=line_chart)  # Set the master as the line chart

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line, data=random_data)  # Display the random data on the line chart
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()

    # Start the main event loop
    root.mainloop()
    ```
    ---

- **Simple style**

    https://github.com/Thisal-D/ctkchart/assets/93121062/afe56452-68c3-44f0-9c67-2ab6f6910f6e

    ``` python
    import customtkinter as ctk  # Importing the customtkinter library as ctk
    import ctkchart  # Importing the ctkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = ctk.CTk()
    root.configure(fg_color="#0d1117")
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = ctkchart.CTkLineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        y_axis_label_count=10, # set y axis labels count to 10
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    # Create a line for the line chart
    line = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        size=2,  # Set the line size to 2
        fill="enabled" # enable line fill
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line, data=random_data)  # Display the random data on the line chart
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()

    # Start the main event loop
    root.mainloop()
    ```
    ---

- **2 lines with different line styles**

    https://github.com/Thisal-D/ctkchart/assets/93121062/9bc35a39-a8ca-4942-9fc7-a1c89d1bd1bc

    ``` python
    import customtkinter as ctk  # Importing the customtkinter library as ctk
    import ctkchart  # Importing the ctkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = ctk.CTk()
    root.configure(fg_color=("#ffffff", "#0d1117"))
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = ctkchart.CTkLineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        y_axis_label_count=10, # set y axis labels count to 10
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    line1 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        color=("#5dffb6","#5dffb6"), # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        style="dashed", # style change to dashed
        style_type=(10, 5), #index 0 for dash width and 1 for space between dashes
    ) 

    line2 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        color=("#FFBAD2", "#FFBAD2"), # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        point_highlight="enabled", # enable point highlight
        point_highlight_color=("#FFBAD2", "#FFBAD2"), # enable point highlight
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line1, data=random_data)  # Display the random data on the line 1 on chart
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line2, data=random_data)  # Display the random data on the line 2 on chart    
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()

    # Start the main event loop
    root.mainloop()
    ```
    ---

- **3 lines with different line styles**

    https://github.com/Thisal-D/ctkchart/assets/93121062/6d568b70-2ceb-42d0-b93c-0096f2745134

    ``` python
    import customtkinter as ctk  # Importing the customtkinter library as ctk
    import ctkchart  # Importing the ctkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = ctk.CTk()
    root.configure(fg_color=("#ffffff", "#0d1117"))
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = ctkchart.CTkLineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        y_axis_label_count=10, # set y axis labels count to 10
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    # Create a line 1 for the line chart
    line1 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        size=2,  # Set the line size to 2
        fill="enabled" # enable line fill
    )  

    line2 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        color=("#5dffb6","#5dffb6"), # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        style="dashed", # style change to dashed
        style_type=(10, 5), #index 0 for dash width and 1 for space between dashes
    ) 

    line3 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        color=("#FFBAD2", "#FFBAD2"), # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        point_highlight="enabled", # enable point highlight
        point_highlight_color=("#FFBAD2", "#FFBAD2"), # enable point highlight
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line1, data=random_data)  # Display the random data on the line 1 on chart
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line2, data=random_data)  # Display the random data on the line 2 on chart
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line3, data=random_data)  # Display the random data on the line 3 on chart
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()

    # Start the main event loop
    root.mainloop()
    ```
    ---

- **Advance** (Actually not, Just Two More Attributes Added)
 
    https://github.com/Thisal-D/ctkchart/assets/93121062/c2838fd6-3a0f-45be-bb39-9953d007067d

    ``` python
    import customtkinter as ctk  # Importing the customtkinter library as ctk
    import ctkchart  # Importing the ctkchart module for chart creation
    import random  # Importing the random module for generating random data
    import threading  # Importing the threading module for running tasks concurrently
    import time  # Importing the time module for adding delays

    # Create the root window and configure
    root = ctk.CTk()
    root.configure(fg_color=("#ffffff", "#0d1117"))
    root.geometry("720x430+200+200")  

    # Create a line chart widget
    line_chart = ctkchart.CTkLineChart(
        master=root,  # Set the master as the root window
        x_axis_values=("01-01", "01-02", "01-03", "01-04", "01-05", "01-06", "01-07", "01-08", "01-09", "01-10"),  # X-axis values
        y_axis_values=(0, 1000),  # Y-axis values (range)
        y_axis_label_count=10, # set y axis labels count to 1
        y_axis_section_count=10,
        x_axis_section_count=10,
    )

    line_chart.pack(pady=15)  # Pack the line chart widget into the root

    line1 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        color=("#5dffb6","#5dffb6"), # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        style="dashed", # style change to dashed
        style_type=(10, 5), #index 0 for dash width and 1 for space between dashes
    ) 

    line2 = ctkchart.CTkLine(
        master=line_chart,  # Set the master as the line chart
        color=("#FFBAD2", "#FFBAD2"), # index 0 for light and 1 for dark theme
        size=2,  # Set the line size to 2
        point_highlight="enabled", # enable point highlight
        point_highlight_color=("#FFBAD2", "#FFBAD2"), # enable point highlight
    )  

    def display_data():
        """Function to continuously display random data on the line chart."""
        while True:
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line1, data=random_data)  # Display the random data on the line 1 on chart
            random_data = [random.choice(range(0, 1000))]  # Generate random data between 0 and 1000
            line_chart.show_data(line=line2, data=random_data)  # Display the random data on the line 2 on chart    
            time.sleep(0.5)  # Pause for 0.5 seconds before the next iteration

    # Call the display_data function as a separate thread
    threading.Thread(target=display_data).start()

    # Start the main event loop
    root.mainloop()
    ```
---

-  #### Light and Dark theme

    **For every parameter that involves color in ctkchart, you can provide either**: 
    - A single string representing the color. 
    - A tuple of two strings where the first string represents the color for the light theme and the second string represents the color for the dark theme.
     
    https://github.com/user-attachments/assets/9fed4b83-5b03-4ea0-82a0-36029dfc93dd

---

**Explore customizable features such as colors, fonts, and more in the documentation.**

#### Please refer to the full documentation
- [**English doc.**](documentation/DOCUMENTATION_en.md)
- [**Chinese doc.**](documentation/DOCUMENTATION_zh.md)

---

#### Contributors
- [<img src="https://github.com/childeyouyu.png?size=25" width="25">](https://github.com/childeyouyu) [youyu](https://github.com/childeyouyu)
